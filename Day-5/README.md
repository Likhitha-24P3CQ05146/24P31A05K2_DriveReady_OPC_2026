# Day 5 – Retrieval-Augmented Generation (RAG)

## Project Overview

This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) system using Python.

The system reads information from a PDF document, converts the extracted text into embeddings, stores them in a FAISS vector database, and uses the Groq API to answer user questions based on the PDF content.

## Technologies Used

- Python
- Sentence Transformers
- FAISS
- Groq API
- PyMuPDF
- Tesseract OCR
- NumPy
- Pillow

## Project Workflow

1. **PDF Text Extraction:** Extract text from the PDF using PyMuPDF. Use Tesseract OCR for scanned pages.
2. **Text Chunking:** Divide the extracted text into smaller chunks of 500 characters with an overlap of 100 characters.
3. **Embedding Generation:** Convert text chunks into numerical vectors using the Sentence Transformer model `all-MiniLM-L6-v2`.
4. **Vector Storage:** Store the generated embeddings in FAISS.
5. **Information Retrieval:** Search for the most relevant text chunks based on the user's question.
6. **Answer Generation:** Use the Groq API to generate answers using the retrieved PDF content.

## Features

- PDF text extraction
- OCR support for scanned documents
- Text chunking with overlapping sections
- Semantic similarity search
- FAISS vector database
- AI-powered question answering
- Interactive question-and-answer system

## Installation

Install the required Python libraries:

```bash
pip install pymupdf sentence-transformers faiss-cpu numpy pillow pytesseract groq
```

Tesseract OCR must also be installed separately on the system for scanned PDF support.

## API Configuration

Set your Groq API key as an environment variable named `GROQ_API_KEY`.

Never share or upload your actual API key to GitHub.

## PDF Input

The program expects a PDF file named:

`Greenwood_Campus_Story.pdf`

Place the PDF in the same folder as `task.py` before running the program.

**Note:** The PDF is used as an input document and is not included in this repository.

## How to Run

Run the following command in the terminal:

```bash
python task.py
```

Ask questions about the PDF document. Type `exit` to end the session.

## Sample Questions

- Who is the principal of Greenwood College?
- How many students and teachers does the college have?
- What are the three main buildings on campus?
- What problem did Dr. Meera Rao notice?

## Expected Output

The system retrieves relevant information from the PDF and generates answers using the Groq API.

If the requested information is not available in the PDF, the system responds:

`The answer is not available in the PDF.`

## Learning Outcomes

- Understanding Retrieval-Augmented Generation (RAG).
- Learning PDF text extraction and OCR.
- Understanding text chunking and embeddings.
- Working with FAISS for vector similarity search.
- Connecting an LLM using the Groq API.
- Building a PDF-based question-answering system.