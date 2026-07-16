from app.data import users, user_id_counter
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(username, email, password):
    global user_id_counter

    for user in users:
        if user["email"] == email:
            return None

    new_user = {
        "id": user_id_counter,
        "username": username,
        "email": email,
        "password": generate_password_hash(password)
    }

    users.append(new_user)
    user_id_counter += 1

    return new_user

def login_user(email, password):
    for user in users:
        if user["email"] == email and check_password_hash(user["password"], password):
            return user
    return None
