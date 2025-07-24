# 🤖 Keerthi's Chatbot

A lightweight, real-time conversational AI chatbot built using **Python** and **Streamlit**, powered by **Google's Gemini Pro API**. This project delivers intelligent, context-aware responses in a clean and user-friendly web interface.

---

## 📌 Overview

**Keerthi's Chatbot** is designed as a simple yet effective interface to interact with Google's powerful generative AI model — Gemini Pro. It securely integrates the API using `Streamlit's secrets.toml` and manages chat history in real time using Streamlit's session state. Ideal for beginners exploring AI or developers seeking to build AI-enabled apps quickly.

---

## 🚀 Features

- 💬 Real-time chatbot interface using Streamlit
- 🔐 Secure API key management with `.toml` and `st.secrets`
- 🧠 Responses powered by **Gemini 1.5 Flash** model
- 🗃️ Persistent chat history within user session
- 🧼 Option to clear and restart conversations easily

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Streamlit**
- **Google Generative AI Python SDK (Gemini)**
- **Pip (for dependency management)**

---

## 📂 Project Structure

├── .streamlit/
│ └── secrets.toml # Secure API key storage
├── chatbot.py # Main application code
├── requirements.txt # Python dependencies
└── README.md # Project documentation

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up your Gemini API key

Create a file .streamlit/secrets.toml and add your Gemini API key:

toml
Copy
Edit
GOOGLE_API_KEY = "your_gemini_api_key_here"
▶️ Run the App
bash
Copy
Edit
streamlit run chatbot.py
The chatbot will launch in your browser.

🚧 Future Improvements
Add voice input and output support

Improve response formatting (Markdown/emoji support)

Add multi-turn conversation memory (context retention)

Support for dark/light theme toggle

## 👩‍💻 Author

**M.B. Sri Keerthi**

- [LinkedIn](https://www.linkedin.com/in/sri-keerthi-maringanti-263957297?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
- [GitHub](https://github.com/Sri-Keerthi-code)





