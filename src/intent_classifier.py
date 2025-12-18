import json
from src.llm_client import call_llm
from src.utils import load_intent_metadata

def classify_intent(user_input):
    intent_names, _ = load_intent_metadata()

    intent_list = "\n".join([f"- {i}" for i in intent_names])

    prompt = f"""
You are an NLU intent classifier.

Allowed intents:
{intent_list}

Rules:
- Choose ONLY one intent from the list
- If none match clearly, choose "general_query"

Return JSON ONLY in this format:
{{
  "intent": "<intent_name>",
  "confidence": <number between 0 and 1>
}}

User input:
"{user_input}"
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "intent": "general_query",
            "confidence": 0.0
        }
