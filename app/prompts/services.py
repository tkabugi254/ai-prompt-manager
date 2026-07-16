from app.data import prompts, prompt_id_counter
from datetime import datetime

def create_prompt(user_id, prompt, category):
    global prompt_id_counter

    new_prompt = {
        "id": prompt_id_counter,
        "user_id": user_id,
        "prompt": prompt,
        "category": category,
        "created_at": str(datetime.utcnow()),
        "usage_count": 0
    }

    prompts.append(new_prompt)
    prompt_id_counter += 1

    return new_prompt