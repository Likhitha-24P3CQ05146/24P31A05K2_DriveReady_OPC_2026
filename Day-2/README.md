# Day 2 – Prompts, Memory and Building My Own AI Chatbot

## Project Overview

Day 2 focuses on understanding prompt engineering, conversation memory and important Python concepts required for building AI-powered applications.

This day consists of two tasks:

1. **Task 1 – Agentic AI Day 2:** Practising prompts, messages, JSON, memory, Python dictionaries, functions, decorators and exception handling.
2. **Task 2 – My Own Chatbot:** Developing a personal AI chatbot using the Groq API that answers questions, follows system instructions and remembers previous conversations.

Both tasks are implemented using Python and the Groq API.

## Objectives

- Understand different message roles: system, user and assistant.
- Learn system prompts and few-shot prompting.
- Generate and process structured JSON responses.
- Implement conversation history and memory.
- Understand Python dictionaries and JSON operations.
- Create functions with type hints and docstrings.
- Learn decorators and exception handling.
- Build a personal AI chatbot using an LLM.

## Technologies Used

- **Programming Language:** Python
- **Platform:** Google Colab
- **AI API:** Groq API
- **Python Library:** Groq Python SDK
- **LLM Model:** `openai/gpt-oss-120b`
- **Data Format:** JSON

## Task 1 – Agentic AI Day 2

Completed the concepts and practical exercises provided in the Day 2 learning material.

### Topics Covered

**1. Messages and Roles**
- System messages
- User messages
- Assistant messages
- Conversation structure

**2. System Prompt**
- Defining the chatbot's role.
- Providing bakery information.
- Setting rules and response formats.

**3. Few-Shot Prompting**
- Providing examples to guide AI responses.
- Classifying customer messages as orders, questions or complaints.

**4. JSON Output and Parsing**
- Generating structured JSON responses.
- Extracting customer order information.
- Using `json.loads()` to convert JSON into Python dictionaries.
- Handling invalid JSON responses.

**5. Conversation Memory**
- Maintaining conversation history.
- Storing user and assistant messages.
- Sending previous messages to the model.
- Trimming older messages using `MAX_TURNS`.

**6. Python Dictionaries and JSON**
- Creating dictionaries.
- Accessing dictionary values.
- Using the `.get()` method.
- Converting dictionaries into JSON using `json.dumps()`.
- Converting JSON back into Python dictionaries.

**7. Functions and Type Hints**
- Creating reusable Python functions.
- Using type hints.
- Writing function docstrings.

**8. Decorators**
- Understanding decorators.
- Creating a logging decorator using `functools.wraps`.
- Tracking function calls.

**9. Exception Handling**
- Using `try` and `except`.
- Handling API rate-limit errors.
- Handling API connection errors.
- Providing user-friendly error messages.

## Task 2 – My Own Personal AI Chatbot

### Project Description

Developed a personal AI chatbot using Python and the Groq API.

The chatbot acts as a friendly personal assistant that answers questions, explains concepts and remembers previous conversation messages.

### Features

- **AI Responses:** Answers user questions using the Groq language model.
- **System Instructions:** Follows predefined personality and response rules.
- **Simple Explanations:** Explains difficult topics in easy English.
- **Step-by-Step Guidance:** Provides examples and explanations whenever necessary.
- **Few-Shot Prompting:** Uses example conversations to guide response generation.
- **JSON Processing:** Generates structured responses and extracts information.
- **Conversation Memory:** Stores previous user and assistant messages.
- **Memory Management:** Maintains recent conversation history.
- **Interactive Assistance:** Helps users with learning and general questions.

### System Prompt

The personal chatbot follows these instructions:

- Be friendly, helpful and intelligent.
- Answer questions in simple English.
- Explain difficult topics step by step.
- Give examples whenever necessary.
- Be polite and supportive.
- If an answer is unknown, say so honestly.
- Keep responses clear and easy to understand.

## How to Run

### Google Colab

1. Open the Day 2 notebook.
2. Install the required library:

   ```python
   !pip install groq
   ```

3. Add your Groq API key to Google Colab Secrets using the name `GROQ_API_KEY`.
4. Import the Groq library.
5. Connect to the Groq API.
6. Execute the notebook cells in order.
7. Test the chatbot using different questions.

### VS Code

1. Install Python.
2. Open the Day-2 folder in VS Code.
3. Install the required library:

   ```bash
   pip install groq
   ```

4. Configure the `GROQ_API_KEY` environment variable.
5. Run the Python file:

   ```bash
   python task.py
   ```

## Sample Chatbot Interaction

**User:** My name is Likhitha.

**Bot:** Nice to meet you, Likhitha! How can I help you today?

**User:** I am learning Python.

**Bot:** That's great! Python is a friendly language to start with.

**User:** What is my name?

**Bot:** Your name is Likhitha.

## Security

- The Groq API key is stored securely.
- API keys are not hardcoded into the Python source file.
- Confidential information should never be uploaded to GitHub.

## Learning Outcomes

After completing Day 2, I learned:

- How to communicate with LLMs using structured messages.
- How to design effective system prompts.
- How few-shot prompting improves response consistency.
- How to generate and process JSON data.
- How to maintain conversation history and memory.
- How to use Python dictionaries, functions and decorators.
- How to handle API errors using exception handling.
- How to develop my own AI chatbot using the Groq API.

## Conclusion

Day 2 helped me understand how prompts, memory and Python programming concepts work together in AI applications.

I successfully completed the provided Agentic AI practical exercises and developed my own Personal AI Chatbot using Python and the Groq API.

This experience provided a foundation for learning AI agents, tool calling and more advanced agentic AI applications in the upcoming tasks.