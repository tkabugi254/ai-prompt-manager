from flask import jsonify
from app.data import prompts
from datetime import datetime

def create_prompt(data, user_id):
    if not data:
        return jsonify({"error": "Missing body please try again......."}), 400

    new_prompt = {
        "id": len(prompts) + 1,
        "user_id": user_id,
        "title": data.get("title"),
        "prompt": data.get("prompt"),
        "category": data.get("category"),
        "tags": data.get("tags", []),
        "favorite": False,
        "usage_count": 0,
        "created_at": str(datetime.now())
    }

    prompts.append(new_prompt)
    return jsonify(new_prompt), 201


def get_prompts(user_id):
    user_prompts = [p for p in prompts if p["user_id"] == user_id]
    return jsonify(user_prompts), 200


def get_prompt(id, user_id):
    for p in prompts:
        if p["id"] == id and p["user_id"] == user_id:
            return jsonify(p), 200
    return jsonify({"error": "No prompt found under that id"}), 404


def update_prompt(id, data, user_id):
    for p in prompts:
        if p["id"] == id and p["user_id"] == user_id:
            p.update(data)
            return jsonify(p), 200
    return jsonify({"error": "No prompt found under that id"}), 404


def delete_prompt(id, user_id):
    for p in prompts:
        if p["id"] == id and p["user_id"] == user_id:
            prompts.remove(p)
            return jsonify({"message": "Deleted thus successfully"}), 200
    return jsonify({"error": "No prompt found under that id"}), 404


def favorite_prompt(id, user_id):
    for p in prompts:
        if p["id"] == id and p["user_id"] == user_id:
            p["favorite"] = True
            return jsonify({"message": "Favorited successfully"}), 200
    return jsonify({"error": "No prompt found under that id"}), 404


def use_prompt(id, user_id):
    for p in prompts:
        if p["id"] == id and p["user_id"] == user_id:
            p["usage_count"] += 1
            return jsonify({"message": "Usage updated successfully"}), 200
    return jsonify({"error": "No prompt found under that id"}), 404


def search_prompts(args, user_id):
    results = [p for p in prompts if p["user_id"] == user_id]

    query = args.get("q")

    if query:
        results = [
            p for p in results
            if query.lower() in (p["title"] or "").lower()
            or query.lower() in (p["category"] or "").lower()
            or query.lower() in " ".join(p["tags"]).lower()
        ]

    return jsonify(results), 200


def get_stats(user_id):
    user_prompts = [p for p in prompts if p["user_id"] == user_id]

    total = len(user_prompts)
    favorites = len([p for p in user_prompts if p["favorite"]])
    usage = sum(p["usage_count"] for p in user_prompts)

    most_used = None
    if user_prompts:
        most_used = max(user_prompts, key=lambda x: x["usage_count"])["title"]

    categories = len(set(p["category"] for p in user_prompts if p["category"]))

    return jsonify({
        "total_prompts": total,
        "favorite_prompts": favorites,
        "total_usage": usage,
        "most_used_prompt": most_used,
        "categories": categories
    }), 200