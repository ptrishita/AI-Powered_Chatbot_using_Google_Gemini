# 🤖 AI-Powered Chatbot using Google Gemini

This project is an interactive AI chatbot built using **Python**, **Streamlit**, and **Google Gemini 2.0 Flash**. The chatbot responds to user inputs in real-time with short, accurate, and context-aware replies. It supports general questions, logic, math, and AI-related queries.

---

## 🔧 Features

- 🌐 Natural language understanding with **Gemini 2.0 Flash**
- ⚡ Fast, relevant responses
- 🧠 Supports factual, logic, math, and AI questions
- 🖥️ Simple user interface built with **Streamlit**
- 🔐 Secure API key management using `.env` file

---

## 📁 Project Structure
```plaintext
AI-Powered_Chatbot_using_Google_Gemini/
│
├── app.py              # Main Streamlit app
├── chatbot.py          # Handles API interaction
├── .env                # Stores Google API key
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ptrishita/AI-Powered_Chatbot_using_Google_Gemini.git
cd AI-Powered_Chatbot_using_Google_Gemini
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Google API Key

- Go to https://ai.google.dev and sign in
- Create an API key for Gemini 2.0 Flash
- Create a .env file in the project root:

```bash
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

## 📚 References
- Google Gemini API: https://ai.google.dev/
- Streamlit Documentation: https://docs.streamlit.io/
- google-generativeai Python Library: https://pypi.org/project/google-generativeai/
- dotenv Python Library: https://pypi.org/project/python-dotenv/

## 🛠️ Future Scope
- Add voice interaction
- Enable chat history and context memory
- Deploy online (e.g., Streamlit Cloud)
- Support for multiple languages

## 📬 Contact
For queries or suggestions, feel free to reach out at [**trishitapaul5@gmail.com**](mailto:trishitapaul5@gmail.com).
