# Day 1 – How LLMs Work and Your First API Call

## Project Overview

This task introduces the fundamentals of Large Language Models (LLMs) and demonstrates how to connect Python with an AI model using the Groq API.

As a practical implementation, an AI-powered customer support chatbot is developed for **Sweet Crumbs Home Bakery**. The chatbot answers customer questions using predefined business facts and instructions.

The task also demonstrates Prompt Injection Detection using Prompt Guard.

## Objectives

- Understand the basic working of Large Language Models (LLMs).
- Learn about tokens, temperature, context windows, memory and hallucinations.
- Connect Python applications to an AI model using the Groq API.
- Create system prompts to control chatbot behaviour.
- Generate fact-based responses using predefined instructions.
- Understand basic prompt injection detection.

## Technologies Used

- **Programming Language:** Python
- **Platform:** Google Colab
- **AI API:** Groq API
- **LLM Integration:** LangChain Groq
- **Chatbot Model:** `openai/gpt-oss-120b`
- **Prompt Guard Model:** `meta-llama/llama-prompt-guard-2-22m`

## Project Implementation

### 1. Groq API Connection

- Installed the required LangChain Groq library.
- Retrieved the Groq API key securely from Google Colab Secrets.
- Connected Python to the Groq language model using `ChatGroq`.

### 2. System Prompt Creation

Created a system prompt for Sweet Crumbs Home Bakery with the following facts and rules:

**Facts:**
- The bakery prepares cakes to order.
- Orders require 24 hours' notice.
- All cakes have eggless versions.

**Rules:**
- Never promise delivery times.
- If the information is unknown, clearly say so.
- Respond politely in fewer than 60 words.

### 3. Chatbot Function

Created an `ask()` function that:
- Accepts a customer's question.
- Sends the system prompt and customer question to the AI model.
- Receives and displays the generated response.

### 4. Chatbot Testing

Tested the chatbot with customer questions about bakery orders and checked whether the responses followed the predefined facts and rules.

### 5. Prompt Injection Detection

Used the Groq SDK with the Prompt Guard model to examine a sample prompt injection attempt and obtain its detection score.

## How to Run

1. Open the Day 1 notebook in Google Colab.
2. Install the required libraries:

   ```python
   !pip install langchain_groq groq
   ```

3. Open Google Colab Secrets.
4. Add your Groq API key with the secret name `GROQ_API_KEY`.
5. Enable notebook access for the secret.
6. Execute the notebook cells in the correct order.
7. Test the chatbot by asking customer-related questions.
8. Execute the Prompt Guard cell to examine the sample prompt injection attempt.

## Sample Chatbot Test

**Input:**

Can I get my order tomorrow?

**Expected Behaviour:**

The chatbot should politely explain that orders require 24 hours' notice and should not guarantee a delivery time.

## Security

- The Groq API key is stored securely in Google Colab Secrets.
- The actual API key is not included in the source code.
- Never upload API keys or other confidential information to GitHub.

## Learning Outcomes

After completing this task, I learned:

- Basic concepts and working principles of LLMs.
- How to connect Python with an AI model using the Groq API.
- How to create and use system prompts.
- How to develop a basic AI-powered chatbot.
- How to use Prompt Guard for examining prompt injection attempts.
- The importance of API key security and responsible AI usage.

## Conclusion

Day 1 provided a practical introduction to Large Language Models and their integration with Python. By developing the Sweet Crumbs Home Bakery chatbot and experimenting with Prompt Guard, I gained a basic understanding of AI-powered applications and prompt security.
