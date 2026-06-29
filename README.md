# 🤖 RuleBot — Python Rule-Based Chatbot

> **Internship Task ** | Built with Python, Flask & HTML/CSS/JS

---

## 📌 Project Overview

RuleBot is a simple rule-based chatbot built using **Python**. It accepts user input and responds with predefined replies using `if-elif` conditions, functions, and loops. The project includes both a **terminal-based** version and a **web-based UI** with a professional dark theme.

---

![alt text](<Screenshot 2026-06-29 215444.png>)

---

## 🗂️ Project Structure

```
chatbot/
├── app.py              ← Flask web server (routes & API)
├── chatbot.py          ← Core chatbot logic (if-elif, functions, loop)
├── templates/
│   └── index.html      ← Frontend web interface (dark theme)
├── static/
│   ├── style.css       ← Styling (dark professional theme)
│   └── script.js       ← Chat interaction logic (fetch API)
└── requirements.txt    ← Python dependencies
```
---

## 💬 Supported Commands

| User Input               | Bot Response                              |
|--------------------------|-------------------------------------------|
| `hello` / `hi` / `hey`  | Hi there! 👋 How can I help you today?   |
| `how are you`            | I'm fine, thanks for asking! 😊           |
| `bye` / `goodbye`        | Goodbye! 👋 Have a wonderful day!        |
| `what is your name`      | I'm RuleBot 🤖 — a Python chatbot!       |
| `what time is it`        | 🕐 The current time is HH:MM AM/PM       |
| `what is today`          | 📅 Today is Day, Month DD, YYYY          |
| `thank you`              | You're welcome! 😊                        |
| `who made you`           | Built by an intern developer using Python!|
| `help`                   | Lists all available commands              |
| *(unknown input)*        | Suggests valid commands to try            |

---

## 🚀 How to Run

### ✅ Option 1 — Terminal Mode (No Flask needed)

```bash
python chatbot.py
```

**Sample Output:**
```
=============================================
       Welcome to RuleBot 🤖
  Type 'bye' to exit | 'help' for commands
=============================================

You: hello
Bot: Hi there! 👋 How can I help you today?

You: how are you
Bot: I'm fine, thanks for asking! 😊 What about you?

You: bye
Bot: Goodbye! 👋 Have a wonderful day!
```

---

### ✅ Option 2 — Web UI Mode (Flask)

**Step 1 — Install Flask:**
```bash
pip install flask
```

**Step 2 — Start the server:**
```bash
python app.py
```

**Step 3 — Open in browser:**
```
http://127.0.0.1:5000
```

---


Install with:
```bash
pip install -r requirements.txt
```

