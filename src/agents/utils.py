import json
#from src.agents.utils import load_intent_metadata

def load_intent_metadata(path="data/intents.json"):
    """
    Loads intent names and entity mapping dynamically
    """
    with open(path, "r") as f:
        data = json.load(f)

    intent_names = []
    intent_entity_map = {}

    for intent in data["intents"]:
        name = intent["name"]
        intent_names.append(name)
        intent_entity_map[name] = intent.get("entities", [])

    return intent_names, intent_entity_map
