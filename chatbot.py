# chatbot.py - Rule-based chatbot logic
# Key Concepts: if-elif, functions

def get_response(user_input):
    """Returns a predefined reply based on user input."""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "howdy"]:
        return "Hi there! 👋 How can I help you today?"

    elif user_input in ["how are you", "how are you doing", "how do you do"]:
        return "I'm fine, thanks for asking! 😊 What about you?"

    elif user_input in ["bye", "goodbye", "see you", "take care", "exit", "quit"]:
        return "Goodbye! 👋 Have a wonderful day!"

    elif user_input in ["what is your name", "who are you", "what are you"]:
        return "I'm RuleBot 🤖 — a simple rule-based chatbot built in Python!"

    elif user_input in ["what can you do", "help", "commands"]:
        return ("I can respond to: 'hello', 'how are you', 'bye', "
                "'what is your name', 'what time is it', and more!")

    elif user_input in ["what time is it", "tell me the time", "current time"]:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"🕐 The current time is {now}."

    elif user_input in ["what is today", "today's date", "what is the date"]:
        from datetime import datetime
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today is {today}."

    elif user_input in ["thank you", "thanks", "thx"]:
        return "You're welcome! 😊 Always happy to help."

    elif user_input in ["who made you", "who created you", "who built you"]:
        return "I was built by an intern developer using Python! 🐍"

    elif user_input == "":
        return "Please type something so I can respond! 💬"

    else:
        return f"I'm not sure how to respond to '{user_input}'. Try: hello, how are you, bye, help."


def run_terminal_chat():
    """Run chatbot in terminal (loop + input/output)."""
    print("=" * 45)
    print("       Welcome to RuleBot 🤖")
    print("  Type 'bye' to exit | 'help' for commands")
    print("=" * 45)

    while True:
        user_input = input("\nYou: ").strip()
        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_terminal_chat()