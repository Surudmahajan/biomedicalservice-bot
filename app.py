from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv("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")
MODEL = "openchat/openchat-3.5-0106"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json.get("message")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "Referer": "https://careerbot.onrender.com",  # Replace with your actual domain if needed
        "X-Title": "CareerBotWeb"
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": user_msg}],
        "temperature": 0.7
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        reply = res.json()["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Sorry, something went wrong!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
