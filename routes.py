
from flask_jwt_extended import get_jwt_identity,jwt_required
from flask import Blueprint,request,jsonify
from models import User,Bookmark,db

routes_bp=Blueprint('routes',__name__,url_prefix='/api')

@routes_bp.route('/bookmarks',methods=['POST'])
@jwt_required()
def create_bookmarks():
    user_id=get_jwt_identity()
    data=request.get_json()
    bookmark=Bookmark(url=data.get('url'),title=data.get('title'),user_id=user_id)
    db.session.add(bookmark)
    db.session.commit()
    return jsonify({'message':'Bookmark created'}),201

@routes_bp.route('/bookmarks',methods=['GET'])
@jwt_required()
def get_bookmarks():
    user_id=get_jwt_identity()
    boomarks=Bookmark.query.filter_by(user_id=user_id).all()
    results=[
        {"id":b.id,"url":b.url,"title":b.title} for b in boomarks
    ]
    return jsonify(results),200

@routes_bp.route('/bookmarks/<int:id>',methods=['DELETE'])
@jwt_required()
def delete_bookmarks(id):
    user_id=get_jwt_identity()
    bookmark=Bookmark.query.get_or_404(id)
    if int(bookmark.user_id)!=int(user_id):
        return jsonify({"error":"forbidden"}),403
    db.session.delete(bookmark)
    db.session.commit()
    return jsonify({"message":"bookmark deleted"}),204