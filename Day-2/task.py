
# ============================================================
# AGENTIC AI - DAY 2
# Prompts, Memory and Python Agents
# Includes Tutorial Exercises + My Personal AI Chatbot
# ============================================================

import os
import json
import functools

from groq import (
    Groq,
    RateLimitError,
    APIConnectionError,
    AuthenticationError
)

MODEL = "openai/gpt-oss-120b"


# ============================================================
# 1. GROQ API CONNECTION
# ============================================================

def get_api_key():
    """Get the Groq API key securely."""

    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        try:
            from google.colab import userdata
            api_key = userdata.get("GROQ_API_KEY")
        except ImportError:
            pass

    if not api_key:
        raise ValueError(
            "Please configure GROQ_API_KEY securely."
        )

    return api_key


client = Groq(api_key=get_api_key())

print("Groq API connected successfully!")


# ============================================================
# 2. MESSAGES AND ROLES
# ============================================================

messages = [
    {"role": "system", "content": "You are a helpful bakery assistant."},
    {"role": "user", "content": "What cakes are available?"},
    {
        "role": "assistant",
        "content": "We have plum cake, chocolate cake and cupcakes."
    },
    {"role": "user", "content": "What is the price of a cupcake?"}
]

print("\n--- Messages and Roles ---")

for message in messages:
    print(message)


# ============================================================
# 3. SYSTEM PROMPT - SWEET CRUMBS BAKERY
# ============================================================

MENU = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80
}

BAKERY_SYSTEM = f"""
ROLE: You are a friendly assistant for Sweet Crumbs Home Bakery.

FACTS:
Menu: {json.dumps(MENU)}
Orders need 24 hours' notice.
All cakes have eggless versions.

RULES:
Never promise a delivery time.
If you don't know something, say "I'll check with the owner."
Remember the customer's name and order during the chat.

FORMAT:
Keep answers under 50 words.
Be friendly and simple.
Reply in English or Telugu according to the customer.
"""

print("\n--- Bakery System Prompt ---")
print(BAKERY_SYSTEM)


# ============================================================
# 4. FEW-SHOT PROMPTING - BAKERY CLASSIFICATION
# ============================================================

def classify_customer_message(new_message):
    """Classify a bakery message using few-shot examples."""

    messages = [
        {
            "role": "system",
            "content": (
                "Label the customer message with one word: "
                "order, question or complaint."
            )
        },

        {"role": "user", "content": "need 2 plum cakes for friday"},
        {"role": "assistant", "content": "order"},

        {"role": "user", "content": "do you have eggless?"},
        {"role": "assistant", "content": "question"},

        {"role": "user", "content": "the cake was dry yesterday"},
        {"role": "assistant", "content": "complaint"},

        {"role": "user", "content": new_message}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content.strip()


# ============================================================
# 5. JSON OUTPUT AND PARSING - BAKERY ORDER
# ============================================================

def extract_bakery_order(customer_message):
    """Extract customer order details in JSON format."""

    system = """
    Extract the order from the customer's message.

    Return ONLY valid JSON with these keys:
    name (text),
    item (text),
    qty (number),
    date (text),
    eggless (true/false).
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": customer_message}
        ],
        temperature=0
    )

    reply = response.choices[0].message.content

    try:
        order = json.loads(reply)

        print("\n--- Extracted Order ---")
        print(json.dumps(order, indent=4))

        return order

    except (json.JSONDecodeError, TypeError):
        print("Invalid JSON response.")
        return None


# ============================================================
# 6. PYTHON DICTIONARIES AND JSON
# ============================================================

student = {
    "name": "Likhitha",
    "course": "Computer Science",
    "year": 2
}

print("\n--- Student Dictionary ---")
print(student)

print("Name:", student["name"])
print("Course:", student["course"])
print("Year:", student["year"])

print("College:", student.get("college", "Not available"))

student_json = json.dumps(student, indent=4)

print("\nStudent JSON:")
print(student_json)

student_data = json.loads(student_json)

print("Student name:", student_data["name"])


# ============================================================
# 7. PYTHON FUNCTIONS AND TYPE HINTS
# ============================================================

def get_price(item: str, qty: int = 1) -> int:
    """Return the total price of an item from the bakery menu."""

    item = item.lower().strip()

    if qty <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if item not in MENU:
        raise KeyError("Item is not available in the menu.")

    return MENU[item] * qty


# ============================================================
# 8. DECORATORS
# ============================================================

def log_call(func):
    """Decorator to display function execution details."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print("Function is starting...")

        result = func(*args, **kwargs)

        print("Function execution completed!")

        return result

    return wrapper


@log_call
def logged_get_price(item: str, qty: int = 1) -> int:
    """Calculate bakery item price with logging."""

    return get_price(item, qty)


# ============================================================
# 9. BAKERY CHATBOT WITH MEMORY AND ERROR HANDLING
# ============================================================

bakery_history = [
    {"role": "system", "content": BAKERY_SYSTEM}
]

MAX_TURNS = 8


def bakery_chat(user_text: str) -> str:
    """Chat with Sweet Crumbs and remember recent messages."""

    bakery_history.append({
        "role": "user",
        "content": user_text
    })

    recent = (
        [bakery_history[0]]
        + bakery_history[1:][-MAX_TURNS:]
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent,
            temperature=0.3
        )

        reply = response.choices[0].message.content

    except RateLimitError:
        reply = "We're a little busy. Please try again in a minute."

    except AuthenticationError:
        reply = "Authentication failed. Please check the API key."

    except APIConnectionError:
        reply = "I can't reach the server right now. Please try again."

    bakery_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply


# ============================================================
# 10. MY PERSONAL AI CHATBOT - DAY 2
# ============================================================

PERSONAL_SYSTEM = """
You are my personal AI assistant.

ROLE:
You are friendly, helpful and intelligent.

RULES:
1. Answer questions in simple English.
2. Explain difficult topics step by step.
3. Give examples whenever necessary.
4. Be polite and supportive.
5. If you don't know an answer, say so honestly.

FORMAT:
Keep answers clear and easy to understand.
"""

personal_history = [
    {"role": "system", "content": PERSONAL_SYSTEM}
]


# Few-shot examples for my personal chatbot
PERSONAL_EXAMPLES = [
    {"role": "user", "content": "Hi, how are you?"},
    {
        "role": "assistant",
        "content": "Hello! I am doing great. How can I help you?"
    },

    {"role": "user", "content": "Explain Python simply."},
    {
        "role": "assistant",
        "content": (
            "Python is a programming language used to build "
            "applications, websites and AI systems."
        )
    },

    {"role": "user", "content": "I am feeling stressed."},
    {
        "role": "assistant",
        "content": (
            "Don't worry! Take a small break. "
            "You can handle things one step at a time."
        )
    }
]


def personal_chat(user_text: str) -> str:
    """Personal chatbot with conversation memory."""

    personal_history.append({
        "role": "user",
        "content": user_text
    })

    recent = (
        [personal_history[0]]
        + personal_history[1:][-MAX_TURNS:]
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent,
            temperature=0.3
        )

        reply = response.choices[0].message.content

    except RateLimitError:
        reply = "Too many requests. Please try again later."

    except AuthenticationError:
        reply = "Invalid API key. Please check your credentials."

    except APIConnectionError:
        reply = "Connection problem. Please try again."

    personal_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply


# ============================================================
# 11. PERSONAL CHATBOT FUNCTION WITH TYPE HINTS
# ============================================================

def chatbot_response(question: str) -> str:
    """Get a response from the personal AI assistant."""

    return personal_chat(question)


# ============================================================
# 12. DECORATOR FOR PERSONAL CHATBOT
# ============================================================

@log_call
def my_chatbot(question: str) -> str:
    """Personal chatbot with function logging."""

    return chatbot_response(question)


# ============================================================
# 13. SAFE CHAT AND PYTHON ERROR HANDLING
# ============================================================

def safe_chat(question: str) -> str:
    """Handle errors while chatting with the personal assistant."""

    try:
        return chatbot_response(question)

    except RateLimitError:
        return "Too many requests. Please try again later."

    except AuthenticationError:
        return "Invalid API key. Please check your credentials."

    except APIConnectionError:
        return "Connection problem. Please try again."

    except Exception as error:
        print("Unexpected error:", error)
        return "Something went wrong. Please try again."


# ============================================================
# 14. MAIN PROGRAM
# ============================================================

def main():

    print("\n===================================")
    print("       AGENTIC AI - DAY 2")
    print("===================================")

    print("\n1. Test Bakery Few-Shot Classification")

    try:
        result = classify_customer_message(
            "Do you deliver near my college?"
        )
        print("Classification:", result)

    except Exception as error:
        print("Classification error:", error)

    print("\n2. Test Bakery Order JSON Extraction")

    try:
        extract_bakery_order(
            "Hi, I am Ravi. I need 2 plum cakes for Friday. "
            "Make them eggless."
        )

    except Exception as error:
        print("Order extraction error:", error)

    print("\n3. Test Bakery Price Function")

    try:
        print("Total for 6 cupcakes:", get_price("cupcake", 6))
        print("Total for 2 plum cakes:", logged_get_price("plum cake", 2))

    except (KeyError, ValueError) as error:
        print(error)

    print("\n4. Test Personal Chatbot")

    answer = safe_chat("Explain Artificial Intelligence simply.")
    print("Chatbot:", answer)

    print("\n5. Personal Chatbot Conversation")
    print("Type 'bye' to return to the main program.\n")

    while True:

        user_text = input("You: ").strip()

        if user_text.lower() in ("bye", "exit", "quit"):
            print("Bot: Thank you for chatting!")
            break

        if user_text:
            print("Bot:", safe_chat(user_text))


if __name__ == "__main__":
    main()
