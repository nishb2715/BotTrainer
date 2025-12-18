import json
from src.llm_client import call_llm
from src.utils import load_intent_metadata

def extract_entities(text, intent):
    _, intent_entity_map = load_intent_metadata()

    entity_list = intent_entity_map.get(intent, [])

    if not entity_list:
        return {}

    prompt = f"""
You are an NLU entity extraction system.

Text:
"{text}"

Extract ONLY these entities:
{entity_list}

Rules:
- Do not guess
- Do not hallucinate
- If nothing found, return empty object

Return JSON ONLY:
{{
  "entities": {{
    "entity_name": "value"
  }}
}}
"""

    response = call_llm(prompt)

    try:
        parsed = json.loads(response)
        return parsed.get("entities", {})
    except json.JSONDecodeError:
        return {}
