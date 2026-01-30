# Chat Assistant 🤖

A full-stack AI Chat application built with **FastAPI** and **React**. This project features a custom user authentication system, persistent chat history using SQLite, and a modular AI logic engine.

## 🚀 Features
* **User Authentication:** Secure registration and login with custom password hashing.
* **Persistent Memory:** Chat history is saved per user in a SQLite database.
* **Responsive UI:** A clean, modern interface built with React.
* **Modular AI Backend:** Currently running a local simulation engine for speed and cost-efficiency.

## 🧠 AI Integration (Open Architecture)
This project is designed to be AI-agnostic. The logic is isolated in `app/ai.py`.
* **Current State:** Uses a local pattern-matching simulator (No API keys needed).
* **Extensibility:** You can easily plug in **Gemini, OpenAI, or Hugging Face** by simply updating the `get_real_ai_response` function in `ai.py`. This makes it easy to upgrade the "brain" of the assistant without touching the frontend or database logic.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, SQLite
* **Frontend:** React, Axios, CSS
* **Authentication:** Custom Hashing Logic

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/sirine50/ai-professional-assistant>
