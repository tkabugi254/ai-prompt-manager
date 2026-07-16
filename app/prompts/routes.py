from flask import Blueprint, request, jsonify
from .services import create_prompt

prompts_bp = Blueprint("prompts", __name__)


@prompts_bp.route("/prompts", methods=["POST"])
def create():
    data = request.get_json()

    prompt = create_prompt(
        data.get("user_id"),
        data.get("prompt"),
        data.get("category")
    )

    return jsonify(prompt), 201


