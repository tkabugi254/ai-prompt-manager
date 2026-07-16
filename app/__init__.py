from flask import Flask
from .auth.routes import auth_bp
from .prompts.routes import prompts_bp

def create_app():
    app = Flask(__name__)

    # simple secret key (no config file needed)
    app.config["SECRET_KEY"] = "supersecretkey"

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(prompts_bp, url_prefix="/api")

    return app