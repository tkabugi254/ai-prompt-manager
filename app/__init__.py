from flask import Flask
from app.auth.routes import auth_bp
from app.prompts.routes import prompts_bp

def create_app():
    app = Flask(__name__)

   

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(prompts_bp, url_prefix="/api/prompts")

    return app