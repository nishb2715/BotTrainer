from src.llm_client import call_llm

print("Sending test request...")
result = call_llm("Return a JSON: {\"working\": true}")
print("\nLLM Response:")
print(result)
