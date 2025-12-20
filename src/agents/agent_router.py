from src.interview_agent import interview_agent

def route_agent(intent_data):
    intent = intent_data.get("intent")

    if intent == "interview_practice":
        return interview_agent()
    else:
        return {
            "message": "Sorry, I cannot handle this request yet."
        }
