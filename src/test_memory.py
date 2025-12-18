from src.memory_manager import update_memory, get_summary

feedback1 = {
    "score": 6,
    "strengths": ["communication"],
    "improvements": ["add examples"]
}

feedback2 = {
    "score": 8,
    "strengths": ["clarity"],
    "improvements": ["be more concise"]
}

update_memory(feedback1)
update_memory(feedback2)

summary = get_summary()
print(summary)
