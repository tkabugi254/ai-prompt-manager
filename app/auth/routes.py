from flask import Blueprint, request, jsonify
from .services import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    user = register_user(
        data.get("username"),
        data.get("email"),
        data.get("password")
    )

    if not user:
        return jsonify({"error": "User already exists"}), 400

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = login_user(
        data.get("email"),
        data.get("password")
    )

    if not user:
        return jsonify({"error": "Username or password incorrect"}), 401

    return jsonify({
        "message": "Login successful",
        "user_id": user["id"]
    }), 200