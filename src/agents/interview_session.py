from src.interview_agent import interview_agent
from src.feedback_agent import feedback_agent
from src.memory_manager import update_memory, get_summary

def run_interview_session(user_answer):
    # 1. Ask a question
    question_data = interview_agent()
    question = question_data["question"]

    print("\nInterview Question:")
    print(question)

    # 2. Evaluate answer
    feedback = feedback_agent(question, user_answer)

    print("\nFeedback:")
    print(feedback)

    # 3. Store in memory
    update_memory(feedback)

    # 4. Show performance summary
    summary = get_summary()

    print("\nPerformance Summary:")
    print(summary)

    return {
        "question": question,
        "feedback": feedback,
        "summary": summary
    }
