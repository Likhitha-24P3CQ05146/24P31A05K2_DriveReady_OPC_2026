# 🍰 Sweet Crumbs Bakery – Agentic AI Order Assistant

An AI-powered bakery assistant built using **Google Gemini, LangChain, Python, and Google Sheets** as part of the Agentic AI Workshop – Day 4.

The assistant helps customers check cake prices, view bakery opening hours, and place orders through a conversational interface. Confirmed orders are stored automatically in Google Sheets.

The same Python program is designed to run in both **VS Code and Google Colab**.

## 🎯 Project Objective

To understand how Agentic AI works by creating an AI agent that can interact with customers, use external tools, validate order details, and save customer orders.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **Google Gemini** – AI language model.
- **LangChain** – Agent creation and tool integration.
- **Google Sheets API** – Stores customer orders.
- **Google Drive API** – Accesses Google Sheets.
- **gspread** – Python library for Google Sheets integration.
- **Pydantic** – Validates customer order information.
- **VS Code and Google Colab** – Development environments.

## 🍰 Bakery Details

### Menu and Prices

| Item | Price |
|---|---:|
| Plum Cake | ₹500 |
| Chocolate Cake | ₹650 |
| Cupcake | ₹80 each |

### Bakery Policies

- Orders require 24 hours' advance notice.
- Eggless cakes are available.
- Sunday opening hours: 10:00 AM – 6:00 PM.
- Other days: 9:00 AM – 8:00 PM.

## ✨ Features

1. **AI Chat Assistant:** Interacts with customers using Gemini.
2. **Price Checking:** Calculates cake prices based on item and quantity.
3. **Opening Hours:** Answers questions about bakery timings.
4. **Order Booking:** Collects customer name, cake item, quantity, date, and eggless preference.
5. **Pydantic Validation:** Checks the structure and validity of order information.
6. **Google Sheets Integration:** Saves customer orders in a spreadsheet.
7. **Automatic Package Installation:** Installs required Python libraries when the program runs.
8. **Cross-Platform Support:** Supports both VS Code and Google Colab.
9. **Error Handling:** Handles errors during agent interaction and order saving.

## 🧠 Day 4 Concepts Implemented

### 1. Why Agents Need Tools

AI agents use tools to perform specific tasks instead of only generating text responses.

### 2. Function Calling

Gemini can decide when to call available tools to retrieve information or perform actions.

### 3. Creating Tools Using `@tool`

LangChain's `@tool` decorator converts Python functions into tools that an AI agent can use.

Tools implemented:

- `get_price()` – Calculates cake prices.
- `is_open()` – Checks bakery opening hours.
- `log_order()` – Validates and saves customer orders.

### 4. Creating an AI Agent

Created an agent using Gemini and LangChain that can understand customer messages and use the available tools.

### 5. Error Handling

Added error handling to manage problems during agent execution and Google Sheets operations.

### 6. Structured Output Using Pydantic

Used a Pydantic `Order` model to organize and validate customer order details.

### 7. Saving Orders to Google Sheets

Connected Python with Google Sheets using `gspread` and saved order details automatically.

### 8. Complete Workflow

Connected the customer chat, AI agent, tools, order validation, and Google Sheets into one application.

## 🔄 Project Workflow

```text
        Customer
            |
            v
     AI Chat Assistant
            |
            v
         Gemini AI
            |
            v
      LangChain Agent
            |
            v
       Available Tools
       /      |       \
      /       |        \
   Price   Opening    Order
   Check    Hours    Booking
                        |
                        v
                  Pydantic Model
                        |
                        v
                  Google Sheets
                        |
                        v
                    Order Saved
```

## 📂 Project Structure

```text
Day-4/
│
├── task.py
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Step 1: Download the Project

Clone the GitHub repository or download the project files.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Day-4
```

### Step 2: Install Required Packages

The `task.py` program automatically installs the required Python packages when executed.

Alternatively, install them manually:

```bash
pip install langchain langchain-google-genai gspread pydantic google-auth google-auth-oauthlib
```

### Step 3: Configure Gemini API Key

Obtain your own Gemini API key from:

[Google AI Studio – Get API Key](https://aistudio.google.com/app/apikey)

The API key must be configured before running the application.

**For VS Code (PowerShell):**

```powershell
$env:GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

**For Google Colab:**

1. Open the Secrets panel in Google Colab.
2. Add a secret named `GOOGLE_API_KEY`.
3. Enter your Gemini API key.
4. Enable notebook access to the secret.

### Step 4: Configure Google Sheets Access

The application connects to the configured Google Spreadsheet.

Spreadsheet access must be configured separately for each environment.

**For VS Code:**

1. Create a Google Cloud project.
2. Enable Google Sheets API.
3. Enable Google Drive API.
4. Configure Google Auth Platform.
5. Create an OAuth Client ID using Desktop App.
6. Download the OAuth JSON credentials.
7. Place the file in the project folder as `credentials.json`.
8. Add your Google account as a test user if the application is in testing mode.

Set the credentials path in PowerShell:

```powershell
$env:GOOGLE_OAUTH_CREDENTIALS="$PWD\credentials.json"
```

**For Google Colab:**

1. Open your notebook in Google Colab.
2. Upload `task.py`.
3. Run the program.
4. Complete Google account authentication when prompted.
5. Allow access to Google Sheets.

The Google account used in Colab must have access to the configured spreadsheet.

### Step 5: Run the Application

**VS Code:**

```bash
python -u task.py
```

**Google Colab:**

```python
%run task.py
```

The application automatically detects the environment and selects the appropriate Google authentication method.

**Note:** The default Gemini model is configured in `task.py`. If it is unavailable for your API account, configure `GEMINI_MODEL` with a model supported by your account.

## 💬 Sample Interactions

### Example 1: Checking Opening Hours

**Customer:**

```text
Are you open on Sunday?
```

**Assistant:**

```text
Yes, we are open on Sunday from
10:00 AM to 6:00 PM!
```

### Example 2: Checking Cake Prices

**Customer:**

```text
How much are 2 chocolate cakes?
```

**Assistant:**

```text
Two chocolate cakes cost Rs 1,300.
Would you like to place an order?
```

### Example 3: Placing an Order

**Customer:**

```text
I'm Likhitha. Please book 2 eggless
plum cakes for 24 Dec.
```

The assistant collects the required details, confirms the order, calculates the total, and saves the order in Google Sheets.

## 📊 Google Sheets Output

The application stores the following information:

| Column | Description |
|---|---|
| name | Customer name |
| item | Cake item |
| qty | Quantity |
| date | Pickup date |
| eggless | Eggless preference |
| total | Total price |

The configured spreadsheet must be accessible to the Google account used to run the application.

Users can configure their own spreadsheet ID using the `SWEET_CRUMBS_SHEET_ID` environment variable.

## 🔐 Security

- Never upload Gemini API keys.
- Never upload `credentials.json`.
- Never upload `token.json`.
- Keep sensitive credentials outside public repositories.
- Use `.gitignore` to exclude private files.
- Use your own API key and Google authentication when running the project.

Example `.gitignore`:

```gitignore
credentials.json
token.json
.env
__pycache__/
*.pyc
```

## ⚠️ Important Note

The 24-hour advance-notice policy is currently included in the AI agent's instructions. It is not independently enforced through Python date validation.

The application requires valid Gemini API access and Google Sheets authentication to perform its complete workflow.

## ✅ Project Testing

The following tests were completed successfully:

- Cake price calculation.
- Bakery opening-hours response.
- Pydantic order validation.
- Gemini AI agent interaction.
- Google Sheets connection.
- Customer order confirmation.
- Saving customer orders to Google Sheets.

## 🎓 Learning Outcomes

Through this project, I learned:

- Why AI agents need tools.
- How function calling works.
- How to create tools using LangChain.
- How to connect Gemini with a LangChain agent.
- How to validate structured data using Pydantic.
- How to integrate Google Sheets with Python.
- How to build an end-to-end AI-powered application.
- How to configure an application for VS Code and Google Colab.

## 👩‍💻 Project Information

**Project:** Sweet Crumbs Bakery – AI Order Assistant

**Workshop:** Agentic AI Workshop – Day 4

**Developer:** Likhitha

**Status:** Successfully implemented and tested.

---

*Built as a hands-on learning project to understand Agentic AI, tool calling, structured data validation, and external API integration.*