from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Get API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"  # You can change model here

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json.get("message")
    print("User Message:", user_msg)
    print("API Key present:", OPENROUTER_API_KEY is not None)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "Referer": "https://careerbot.onrender.com",  # Replace with your domain if needed
        "X-Title": "CareerBotWeb"
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": user_msg}],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=headers, json=payload)
        print("Status Code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Sorry, something went wrong."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
