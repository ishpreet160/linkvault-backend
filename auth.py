from flask import Blueprint,request,jsonify
from flask_jwt_extended import create_access_token
from extensions import db
from datetime import timedelta
from models import db, User

auth_bp=Blueprint('auth',__name__,url_prefix='/api/auth')

@auth_bp.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    if not data:
        return jsonify(message="no input data"),400
    
    email=data.get('email')
    password=data.get('password')
    
    if not all([email,password]):
        return jsonify(message="email,password are required")
    
    if User.query.filter_by(email=email).first():
        return jsonify(message="user already exists"), 400
    try:
        new_user=User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="registered succesefully"),201
    except Exception as e:
        db.session.rollback()
        return jsonify(message=str(e)),500
    
@auth_bp.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    if not data: return jsonify(message="Misising Json"),400
    user=User.query.filter_by(email=data.get('email')).first()
    if user and user.check_password(data.get('password')):
        token = create_access_token(
            identity=str(user.id), 
            expires_delta=timedelta(hours=24)
        )
        return jsonify({
            'access_token':token,
            'user':{
                'id':user.id,
                'email': user.email
            }
        }),200
    return jsonify(message='invalid'),401
    