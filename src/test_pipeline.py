from src.intent_classifier import classify_intent
from src.agent_router import route_agent

user_input = "I want to practice interview questions"

intent = classify_intent(user_input)
print("Intent:", intent)

agent_response = route_agent(intent)
print("\nAgent Response:")
print(agent_response)
