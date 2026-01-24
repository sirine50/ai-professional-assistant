# ai_logic.py
def get_mock_ai_response(question: str):
    question = question.lower()
    if "hello" in question:
        return "Hello! I am your AI assistant. I'm currently running in 'Simple Mode'."
    elif "help" in question:
        return "I can help you with coding or answering basic questions!"
    return f"Processed your request: '{question}'. System connection: STABLE."