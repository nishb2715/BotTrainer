from src.llm_client import call_llm
import json

def interview_agent():
    prompt = """
You are an interview coach.

Ask ONE behavioral interview question.
Return output as JSON only in this format:
{
  "question": "<interview question>",
  "category": "behavioral"
}
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "question": "Tell me about yourself.",
            "category": "behavioral"
        }
