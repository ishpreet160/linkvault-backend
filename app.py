from flask import Flask
from flask_cors import CORS, cross_origin
from config import Config
from routes import routes_bp
from extensions import db,jwt
from auth import auth_bp
def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(auth_bp,url_prefix='//api/auth')
    app.register_blueprint(routes_bp)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
     return {"message": "API is running!"}, 200

    return app

app=create_app()
if __name__=="__main__":
    app.run(debug=True)





