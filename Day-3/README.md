# Agentic AI Workshop – Day 3
## Building an AI Bakery Assistant Using LangChain

### 📌 Project Overview
This project is part of Day 3 of the Agentic AI Workshop. It focuses on understanding AI Agents and building a bakery customer-support assistant using **LangChain and Google Gemini**.

The assistant is designed for **Sweet Crumbs Home Bakery** to answer customer questions about cake prices, eggless options, order requirements, and other bakery-related queries.

### 🎯 Learning Objectives
- Understand the difference between chatbots and AI agents.
- Learn the four components of an AI agent: Brain, Instructions, Tools, and Memory.
- Understand the Agent Loop: Think → Act → Observe → Repeat.
- Explore the three levels of AI: Traditional AI, Generative AI, and Agentic AI.
- Understand LangChain fundamentals.
- Build an LLM-powered assistant using a prompt template and model.
- Implement conversation history and memory.
- Create CSV-based test cases to evaluate assistant responses.
- Explore AI agent creation using LangChain.

### 🛠️ Technologies Used
- Python
- LangChain
- Google Gemini API
- Pandas
- CSV

### 🏪 Business Scenario: Sweet Crumbs Home Bakery

The assistant follows these bakery details:

| Product / Rule | Details |
|---|---|
| Plum Cake | ₹500 |
| Chocolate Cake | ₹650 |
| Cupcake | ₹80 each |
| Advance Notice | 24 hours |
| Eggless Options | Available for all cakes |

### ✨ Features Implemented

**1. Bakery Assistant**
- Answers customer questions about bakery products.
- Provides cake prices and calculates order totals.
- Responds to eggless cake queries.
- Follows the bakery's ordering rules.

**2. Custom System Prompt**
- Defines the assistant's role and responsibilities.
- Provides bakery information and business rules.
- Keeps responses friendly and under 50 words.
- Supports English and Telugu according to the customer's language.

**3. Conversation Memory**
- Stores previous customer questions and assistant responses.
- Uses conversation history to maintain context.

**4. CSV-Based Testing**
- Contains 10 customer questions.
- Uses expected keywords to check responses.
- Helps evaluate the assistant's response accuracy.

**5. Temperature Experiment**
- Explores the effect of temperature 1.0 on AI responses.
- Compares responses to observe variations.

**6. AI Agent Preview**
- Creates an AI agent using LangChain's `create_agent`.
- Uses an empty tools list as an introduction to agent creation.
- Actual tool integration is planned for Day 4.

**7. Python Utility Functions**
- `get_cake_price()` – Returns the price of a bakery product.
- `is_order_notice_valid()` – Checks the 24-hour advance-order requirement.

### 📂 Project Structure

```text
Agentic-AI-Day-3/
│
├── task.py
├── tests.csv
└── README.md
```

### ⚙️ Installation and Setup

**Step 1: Install the required packages**

```bash
pip install langchain langchain-google-genai pandas
```

**Step 2: Configure the Gemini API key**

Set your API key as an environment variable.

For Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
```

Never upload your actual API key to GitHub.

**Step 3: Run the Python file**

```bash
python task.py
```

### 🧪 Testing

The project includes 10 customer questions in `tests.csv` to evaluate the assistant.

Example test cases:

| Customer Question | Expected Keyword |
|---|---|
| How much is a plum cake? | 500 |
| Do you make eggless cakes? | eggless |
| What is the price of 6 cupcakes? | 480 |
| How much is a chocolate cake? | 650 |
| Can I order a cake for tomorrow? | 24 hours |

The project also includes Python function tests that can run without making Gemini API calls.

**Note:** Live Gemini response testing and the temperature experiment require API access and available Gemini quota.

### 📚 Key Concepts Learned

- Chatbot vs AI Agent
- Agent Architecture
- Agent Loop
- Traditional AI, Generative AI, and Agentic AI
- LangChain Models
- Prompt Templates
- Chains
- Conversation Memory
- CSV-Based Evaluation
- AI Agent Creation

### 🚀 Future Scope

- Integrate real bakery tools into the AI agent.
- Add customer order management.
- Connect the assistant to a bakery database.
- Implement automated order tracking.
- Improve response evaluation and accuracy.

### 👩‍💻 Workshop Progress

**Day 3 – Completed Offline Implementation**

This project demonstrates the fundamentals of building an LLM-powered business assistant using LangChain and Google Gemini.

---

*Agentic AI Workshop | Day 3 | Sweet Crumbs Home Bakery*