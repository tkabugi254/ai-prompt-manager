from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.prompts.services import *

prompts_bp = Blueprint("prompts", __name__)

@prompts_bp.route("", methods=["POST"])
@jwt_required()
def create():
    return create_prompt(request.get_json(), get_jwt_identity())

@prompts_bp.route("", methods=["GET"])
@jwt_required()
def get_all():
    return get_prompts(get_jwt_identity())

@prompts_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_one(id):
    return get_prompt(id, get_jwt_identity())

@prompts_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    return update_prompt(id, request.get_json(), get_jwt_identity())

@prompts_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return delete_prompt(id, get_jwt_identity())

@prompts_bp.route("/<int:id>/favorite", methods=["PATCH"])
@jwt_required()
def favorite(id):
    return favorite_prompt(id, get_jwt_identity())

@prompts_bp.route("/<int:id>/use", methods=["PATCH"])
@jwt_required()
def use(id):
    return use_prompt(id, get_jwt_identity())

@prompts_bp.route("/search", methods=["GET"])
@jwt_required()
def search():
    return search_prompts(request.args, get_jwt_identity())

@prompts_bp.route("/statistics", methods=["GET"])
@jwt_required()
def stats():
    return get_stats(get_jwt_identity())