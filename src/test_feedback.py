from src.feedback_agent import feedback_agent

question = "Tell me about a time you faced a difficult challenge."
answer = "I stayed calm, analyzed the problem, and worked with my team to solve it."

result = feedback_agent(question, answer)
print(result)
