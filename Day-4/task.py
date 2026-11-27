
"""
Day 4 - Sweet Crumbs Home Bakery AI Agent
Works in Google Colab and VS Code.
"""

# ------------------------------------------------------------
# 0. INSTALL REQUIRED PACKAGES AUTOMATICALLY
# ------------------------------------------------------------

import sys
import subprocess

required_packages = [
    "langchain",
    "langchain-google-genai",
    "gspread",
    "pydantic",
    "google-auth",
    "google-auth-oauthlib",
]

subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    *required_packages
])

import os
from typing import Literal

import gspread
from pydantic import BaseModel, Field
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


# ------------------------------------------------------------
# 1. BAKERY MENU AND OPENING HOURS
# ------------------------------------------------------------

MENU = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80,
}

HOURS = {
    "monday": "9 am to 8 pm",
    "tuesday": "9 am to 8 pm",
    "wednesday": "9 am to 8 pm",
    "thursday": "9 am to 8 pm",
    "friday": "9 am to 8 pm",
    "saturday": "9 am to 8 pm",
    "sunday": "10 am to 6 pm",
}

SHEET_ID = os.getenv(
    "SWEET_CRUMBS_SHEET_ID",
    "1UrjdmtHEvQ9arpwurAufBGWJUdgAxA4HWsN1Wp4kx_s"
)


# ------------------------------------------------------------
# 2. GET GEMINI API KEY
# ------------------------------------------------------------

def get_gemini_api_key():
    """Get the API key from Colab Secrets or local environment."""

    # Google Colab
    try:
        from google.colab import userdata

        key = userdata.get("GOOGLE_API_KEY")

        if key:
            return key

    except Exception:
        pass

    # VS Code / Local Python
    key = os.getenv("GOOGLE_API_KEY")

    if key:
        return key

    raise RuntimeError(
        "GOOGLE_API_KEY not found. "
        "Add it to Colab Secrets or set it in VS Code."
    )


# ------------------------------------------------------------
# 3. CONNECT TO GOOGLE SHEETS
# ------------------------------------------------------------

def connect_google_sheets():
    """Automatically connect using Colab or VS Code authentication."""

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    # Detect Google Colab
    try:
        from google.colab import auth
        IN_COLAB = True

    except ImportError:
        IN_COLAB = False

    # Google Colab authentication
    if IN_COLAB:

        from google.auth import default

        print("Google Colab detected.")
        print("Please complete Google sign-in if requested.")

        auth.authenticate_user()

        credentials, _ = default(scopes=scopes)

        client = gspread.authorize(credentials)

    # VS Code authentication
    else:

        print("VS Code / Local Python detected.")

        credentials_file = os.getenv(
            "GOOGLE_OAUTH_CREDENTIALS"
        )

        if credentials_file:

            if not os.path.isfile(credentials_file):
                raise FileNotFoundError(
                    "Google OAuth credentials file not found."
                )

            client = gspread.oauth(
                credentials_filename=credentials_file
            )

        else:
            # Uses gspread's default OAuth credentials location.
            client = gspread.oauth()

    # Connect to the existing spreadsheet
    spreadsheet = client.open_by_key(SHEET_ID)

    worksheet = spreadsheet.sheet1

    # Add headings if the sheet is empty
    headings = [
        "name",
        "item",
        "qty",
        "date",
        "eggless",
        "total",
    ]

    if not worksheet.row_values(1):
        worksheet.append_row(headings)

    print("Google Sheets connected successfully!")
    print("Spreadsheet:", spreadsheet.url)

    return worksheet


# ------------------------------------------------------------
# 4. PYDANTIC ORDER STRUCTURE
# ------------------------------------------------------------

class Order(BaseModel):
    """Structure used to validate customer orders."""

    name: str = Field(
        description="Customer's first name",
        min_length=1
    )

    item: Literal[
        "plum cake",
        "chocolate cake",
        "cupcake"
    ]

    qty: int = Field(
        description="Quantity of cakes",
        ge=1
    )

    date: str = Field(
        description="Customer's pickup date",
        min_length=1
    )

    eggless: bool = Field(
        description="True if eggless cake is requested"
    )


# ------------------------------------------------------------
# 5. CONNECT TO GEMINI
# ------------------------------------------------------------

api_key = get_gemini_api_key()

model_name = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)

llm = ChatGoogleGenerativeAI(
    model=model_name,
    google_api_key=api_key,
    temperature=0.2,
    max_retries=3,
)

print("Gemini model configured:", model_name)


# ------------------------------------------------------------
# 6. GOOGLE SHEETS CONNECTION
# ------------------------------------------------------------

ws = connect_google_sheets()


# ------------------------------------------------------------
# 7. CREATE BAKERY TOOLS
# ------------------------------------------------------------

@tool
def get_price(item: str, qty: int = 1) -> str:
    """Calculate the total price of a bakery item.

    Args:
        item: plum cake, chocolate cake or cupcake.
        qty: Quantity required.
    """

    item_key = item.lower().strip()

    if item_key not in MENU:
        return (
            f"{item} is not available. "
            f"Available items: {', '.join(MENU)}."
        )

    if qty < 1:
        return "Quantity must be at least 1."

    total = MENU[item_key] * qty

    return f"{qty} x {item_key} = Rs {total}"


@tool
def is_open(day: str) -> str:
    """Check the bakery opening hours for a particular weekday."""

    day_key = day.lower().strip()

    hours = HOURS.get(day_key)

    if hours:
        return f"Open {hours} on {day_key}."

    return "Please provide a valid day of the week."


@tool
def log_order(
    name: str,
    item: str,
    qty: int,
    date: str,
    eggless: bool,
) -> str:
    """Save a confirmed customer order to Google Sheets.

    Use this tool only after collecting all required details
    and receiving clear confirmation to place the order.
    """

    try:
        order = Order(
            name=name.strip(),
            item=item.lower().strip(),
            qty=qty,
            date=date.strip(),
            eggless=eggless,
        )

    except Exception as error:
        return f"Order validation failed: {error}"

    total = MENU[order.item] * order.qty

    try:
        ws.append_row([
            order.name,
            order.item,
            order.qty,
            order.date,
            "yes" if order.eggless else "no",
            total,
        ])

    except Exception as error:
        print("Google Sheets error:", error)

        return (
            "The order could not be saved. "
            "Please try again later."
        )

    return (
        f"Order successfully saved! "
        f"{order.qty} x {order.item} for {order.name}. "
        f"Pickup date: {order.date}. "
        f"Eggless: {'Yes' if order.eggless else 'No'}. "
        f"Total: Rs {total}."
    )


# ------------------------------------------------------------
# 8. CREATE THE AI AGENT
# ------------------------------------------------------------

SYSTEM = """
ROLE:
You are the friendly AI order assistant for
Sweet Crumbs Home Bakery.

BAKERY MENU:
- Plum cake: Rs 500
- Chocolate cake: Rs 650
- Cupcake: Rs 80 each

BAKERY POLICIES:
- Orders require 24 hours' advance notice.
- Eggless versions are available for all cakes.
- Sunday opening hours are 10 am to 6 pm.

RULES:
1. Always use get_price to calculate prices.
2. Always use is_open to check opening hours.
3. Never guess prices or opening hours.
4. Collect the customer's name, item, quantity
   and pickup date before placing an order.
5. Ask for missing information.
6. Save an order only when the customer clearly
   confirms that they want to place it.
7. Never claim an order is saved unless log_order
   reports successful saving.
8. Respect the 24-hour advance-notice policy.
9. If an item is unavailable, explain the menu.
10. Read the confirmed order details and total
    back to the customer after saving.

LANGUAGE:
Reply in English or Telugu, matching the customer.

STYLE:
Keep replies friendly, simple and under 60 words.
"""

tools = [
    get_price,
    is_open,
    log_order,
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM,
)


# ------------------------------------------------------------
# 9. CHAT FUNCTION
# ------------------------------------------------------------

history = []


def chat(user_text: str) -> str:
    """Send a message to Gemini and return its response."""

    global history

    try:

        result = agent.invoke({
            "messages": history + [
                {
                    "role": "user",
                    "content": user_text,
                }
            ]
        })

        history = result["messages"]

        final_message = history[-1].content

        if isinstance(final_message, str):
            return final_message

        if isinstance(final_message, list):

            text_parts = []

            for block in final_message:

                if isinstance(block, dict):

                    if block.get("type") == "text":
                        text_parts.append(
                            block.get("text", "")
                        )

                elif hasattr(block, "text"):
                    text_parts.append(block.text)

            return "\n".join(text_parts)

        return str(final_message)

    except Exception as error:

        print("Agent error:", error)

        return (
            "Sorry, the AI service is temporarily unavailable. "
            "Please try again."
        )


# ------------------------------------------------------------
# 10. RUN THE CHAT APPLICATION
# ------------------------------------------------------------

def main():

    print("\n--- Local Tool Checks ---")

    print(
        get_price.invoke({
            "item": "plum cake",
            "qty": 2
        })
    )

    print(
        is_open.invoke({
            "day": "sunday"
        })
    )

    sample_order = Order(
        name="Likhitha",
        item="plum cake",
        qty=2,
        date="24 Dec",
        eggless=True,
    )

    print("Pydantic validation:", sample_order)

    print(
        "Sample total: Rs",
        MENU[sample_order.item] * sample_order.qty
    )

    print("\n--- Sweet Crumbs AI Chat ---")

    print("Type 'exit' to stop.")

    print("Try: Are you open on Sunday?")

    print("Try: How much are 2 chocolate cakes?")

    print(
        "Try: I'm Likhitha. Please book "
        "2 eggless plum cakes for 24 Dec."
    )

    while True:

        try:
            user_message = input("\nYou: ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Thank you for visiting Sweet Crumbs!")
            break

        if user_message.lower() in {
            "exit",
            "quit",
            "bye"
        }:

            print(
                "Bot: Thank you for visiting "
                "Sweet Crumbs Home Bakery!"
            )

            break

        if not user_message:

            print("Bot: Please enter a message.")

            continue

        print("Bot:", chat(user_message))


if __name__ == "__main__":
    main()
