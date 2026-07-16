from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.data import users

def register_user(data):
    if not data:
        return jsonify({"error": "Missing body please try again......"}), 400

    required = ["username", "email", "password"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} required"}), 400

    for user in users:
        if user["email"] == data["email"]:
            return jsonify({"error": "Email already exists try using a diffrent email or login"}), 400

    new_user = {
        "id": len(users) + 1,
        "username": data["username"],
        "email": data["email"],
        "password": generate_password_hash(data["password"])
    }

    users.append(new_user)

    return jsonify({"message": "User registered"}), 201


def login_user(data):
    if not data:
        return jsonify({"error": "Missing body please try again.........."}), 400

    for user in users:
        if user["username"] == data["username"] and check_password_hash(user["password"], data["password"]):

            access_token = create_access_token(identity=str(user["id"]))  

            return jsonify({
                "access_token": access_token
            }), 200

    return jsonify({"error": "Username or password incorrect"}), 401