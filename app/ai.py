import random
import time

def get_real_ai_response(prompt: str) -> str:
    """
    Simulates an AI response using logic patterns and randomized templates.
    No API key required, 100% free, 0ms latency.
    """
    prompt = prompt.lower().strip()
    
    # Pattern 1: Greetings
    if any(word in prompt for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice([
            "System online. Hello, User. How can I assist you today?",
            "Greetings. Accessing local logic gates... How can I help?",
            "Hello! I am the Nexus Chat Assistant. Ready for your commands."
        ])

    # Pattern 2: Identity
    if "who are you" in prompt or "your name" in prompt:
        return "I am the Nexus Logic Engine. I am a simulated intelligence running locally on your FastAPI server."

    # Pattern 3: Capability
    if "what can you do" in prompt or "help" in prompt:
        return "I can simulate conversation, provide system status, and help you test your database logic."

    # Pattern 4: Time/Date
    if "time" in prompt or "date" in prompt:
        from datetime import datetime
        now = datetime.now()
        return f"System clock check: It is currently {now.strftime('%A, %B %d, %Y at %H:%M:%S')}."

    # Pattern 5: Math (Simple Simulator)
    if any(op in prompt for op in ["+", "-", "*", "/"]):
        return "I detected a mathematical request. While I'm in simulation mode, please use a calculator for precision, but I'm impressed by the query!"

    # Fallback: The "Thinking" Simulator
    responses = [
        f"Processing query: '{prompt}'... Logic confirmed. However, my local knowledge base is limited to system operations.",
        "Interesting inquiry. I have logged this to the Nexus database for further analysis.",
        "I understand the request, but I require more processing modules to answer that fully.",
        "Analysis complete. The probability of success is high, though I cannot provide specifics in this version."
    ]
    return random.choice(responses)