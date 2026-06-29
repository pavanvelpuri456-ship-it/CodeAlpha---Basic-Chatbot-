# app.py - Flask web server
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        user_message = data.get("message", "")
        bot_reply = get_response(user_message)
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": "Server error: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)