from flask import Flask
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    jwt.init_app(app)

    from app.auth.routes import auth_bp
    from app.prompts.routes import prompts_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(prompts_bp, url_prefix="/api/prompts")

    return app