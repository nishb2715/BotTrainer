import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"sessions": []}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory(feedback):
    memory = load_memory()

    session = {
        "score": feedback.get("score", 0),
        "strengths": feedback.get("strengths", []),
        "improvements": feedback.get("improvements", [])
    }

    memory["sessions"].append(session)
    save_memory(memory)

def get_summary():
    memory = load_memory()
    sessions = memory["sessions"]

    if not sessions:
        return {"average_score": 0, "common_weaknesses": []}

    avg_score = sum(s["score"] for s in sessions) / len(sessions)

    weaknesses = []
    for s in sessions:
        weaknesses.extend(s["improvements"])

    return {
        "average_score": round(avg_score, 2),
        "common_weaknesses": list(set(weaknesses))
    }
