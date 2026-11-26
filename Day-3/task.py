
"""
Agentic AI Workshop - Level 2 - Day 3
Project: Sweet Crumbs Home Bakery Assistant

Day 3 topics:
1. LangChain model setup
2. Prompt template
3. Chain creation
4. Conversation memory
5. CSV testing with 10 questions
6. Temperature experiment
7. AI agent creation
8. Python functions for Day 4 tools
"""

import os
import csv
from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent


# ---------------------------------------
# 1. BAKERY SYSTEM PROMPT
# ---------------------------------------

SYSTEM = """
ROLE:
You are a friendly assistant for Sweet Crumbs Home Bakery.

FACTS:
- Plum cake costs Rs 500.
- Chocolate cake costs Rs 650.
- Cupcake costs Rs 80 each.
- Orders require 24 hours' notice.
- All cakes have eggless versions.

RULES:
1. Never promise a delivery time or place.
2. If information is unknown, say:
   "I'll check with the owner."
3. Calculate totals carefully.
4. Keep customer information in conversation history.

FORMAT:
- Keep answers under 50 words.
- Be friendly and polite.
- Reply in English or Telugu, matching the customer.
"""


# ---------------------------------------
# 2. GEMINI MODEL SETUP
# ---------------------------------------

def get_model(temperature: float = 0.3):
    """Create a Gemini model using the secure API key."""

    try:
        from google.colab import userdata
        api_key = userdata.get("GOOGLE_API_KEY")
    except ImportError:
        api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not configured.")

    return ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=temperature,
        timeout=30,
        max_retries=0
    )


# ---------------------------------------
# 3. LANGCHAIN PROMPT TEMPLATE
# ---------------------------------------

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])


# ---------------------------------------
# 4. CREATE LANGCHAIN CHAIN
# ---------------------------------------

def create_bakery_chain(model):
    """Connect the prompt, language model and output parser."""

    return prompt | model | StrOutputParser()


# ---------------------------------------
# 5. CONVERSATION MEMORY
# ---------------------------------------

history = []


def ask(chain, question: str) -> str:
    """Ask a question and remember the conversation."""

    answer = chain.invoke({
        "history": history,
        "question": question
    })

    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=answer))

    return answer


# ---------------------------------------
# 6. CREATE 10 CUSTOMER TEST QUESTIONS
# ---------------------------------------

TESTS_FILE = Path(__file__).with_name("tests.csv")

TEST_QUESTIONS = [
    ("How much is a plum cake?", "500"),
    ("Do you make eggless cakes?", "eggless"),
    ("Can I get a cake today evening?", "24 hours"),
    ("Do you deliver to Kakinada?", "check with the owner"),
    ("What is the price of 6 cupcakes?", "480"),
    ("How much is a chocolate cake?", "650"),
    ("What is the price of 3 plum cakes?", "1500"),
    ("Can I order an eggless chocolate cake?", "eggless"),
    ("How much do 2 cupcakes cost?", "160"),
    ("Can I order a cake for tomorrow?", "24 hours")
]


def create_tests_csv():
    """Create tests.csv containing 10 customer questions."""

    with open(TESTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["question", "must_include"])
        writer.writerows(TEST_QUESTIONS)

    print("tests.csv created successfully!")


# ---------------------------------------
# 7. TEST THE ASSISTANT
# ---------------------------------------

def run_tests(chain):
    """Test customer questions and calculate the pass rate."""

    passed = 0
    total = 0

    with open(TESTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            question = row["question"]
            expected = row["must_include"].lower()

            print("\nQuestion:", question)

            answer = chain.invoke({
                "history": [],
                "question": question
            })

            print("Answer:", answer)

            total += 1

            if expected in answer.lower():
                print("PASS")
                passed += 1
            else:
                print("FAIL")

    print("\nTotal tests:", total)
    print("Passed:", passed)
    print("Pass rate:", round(passed / total * 100, 2), "%")


# ---------------------------------------
# 8. TEMPERATURE EXPERIMENT
# ---------------------------------------

def temperature_experiment():
    """Compare two responses using temperature 1.0."""

    creative_model = get_model(temperature=1.0)
    creative_chain = create_bakery_chain(creative_model)

    question = "Suggest a friendly message for a cake customer."

    print("First response:")
    print(creative_chain.invoke({
        "history": [],
        "question": question
    }))

    print("\nSecond response:")
    print(creative_chain.invoke({
        "history": [],
        "question": question
    }))


# ---------------------------------------
# 9. CREATE DAY 3 AI AGENT
# ---------------------------------------

def create_bakery_agent(model):
    """Create an AI agent with no tools for the Day 3 preview."""

    return create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEM
    )


# ---------------------------------------
# 10. TWO PYTHON FUNCTIONS
# ---------------------------------------

def get_cake_price(cake_name: str) -> int | None:
    """Return the cake price or None if the cake is unavailable."""

    prices = {
        "plum cake": 500,
        "chocolate cake": 650,
        "cupcake": 80
    }

    return prices.get(cake_name.lower().strip())


def is_order_notice_valid(hours_before_order: int) -> bool:
    """Check whether an order meets the 24-hour notice requirement."""

    return hours_before_order >= 24


# ---------------------------------------
# 11. MAIN PROGRAM
# ---------------------------------------

if __name__ == "__main__":

    print("Sweet Crumbs - Agentic AI Day 3")

    print("\nTesting Python functions:")

    print("Plum cake price:", get_cake_price("plum cake"))
    print("Chocolate cake price:", get_cake_price("chocolate cake"))
    print("Six cupcake total:", 6 * get_cake_price("cupcake"))

    print("24-hour notice:", is_order_notice_valid(24))
    print("12-hour notice:", is_order_notice_valid(12))

    create_tests_csv()

    print("\nDay 3 offline setup completed.")
    print("Gemini calls are not started automatically.")
