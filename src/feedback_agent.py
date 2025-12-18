from src.llm_client import call_llm
import json

def feedback_agent(question, answer):
    prompt = f"""
You are an interview evaluator.

Evaluate the candidate's answer.

Interview Question:
"{question}"

Candidate Answer:
"{answer}"

Return ONLY JSON in the following format:
{{
  "score": <number between 0 and 10>,
  "strengths": ["point1", "point2"],
  "improvements": ["point1", "point2"]
}}
"""

    response = call_llm(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {
            "score": 0,
            "strengths": [],
            "improvements": ["Unable to evaluate answer."]
        }
