
# 🧬 Biomedical Service Bot
**Biomedical Service Bot** is a smart AI-powered biomedical guidance chatbot built with **Flask** and **OpenRouter API**, designed to help users receive instant biomedical-related advice and suggestions.

<img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/d669f760-dd10-4dab-8459-643ea32fd807" />


---

## ✨ Features

- 🔗 Powered by [OpenRouter.ai](https://openrouter.ai)
- 🧠 Uses the `mistralai/mistral-7b-instruct` LLM
- ⚡ Simple and clean web UI
- 🌐 Fully deployed on [Render](https://render.com)
- 🔐 API key hidden using environment variables

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **LLM API**: OpenRouter API (Mistral-7B)
- **Deployment**: Render (can also be deployed to Netlify + Flask backend separately)

---

## 📂 Project Structure

```bash
careerbot-web/
├── templates/
│   └── index.html      # Frontend UI
├── static/             # (Optional) CSS/JS assets
├── app.py              # Flask backend with API integration
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/careerbot-web.git
cd careerbot-web
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your OpenRouter API Key
Set your environment variable:
```bash
export OPENROUTER_API_KEY=your-api-key-here
```
> On Windows (CMD):
```cmd
set OPENROUTER_API_KEY=your-api-key-here
```

### 4. Run the App
```bash
python app.py
```
Visit `http://localhost:10000`

---

## 🧪 Sample Prompt
User: *"I'm feeling lightheaded and dizzy after standing up. What could be the reason?"*

Biomedical Service Bot: *"It could be due to a condition called orthostatic hypotension, which occurs when your blood pressure drops upon standing up, causing dizziness and lightheadedness...."*

---

## 🌍 Live Demo
**Check it live at:** [https://biomedicalservice-bot.onrender.com/](https://biomedicalservice-bot.onrender.com/)

> ⚠️ *Note: This site is hosted on Render's free tier and may go offline due to inactivity. Please refresh the page after a few seconds if it appears down.*

---

## 🙌 Credits
- Built by **Surud Mahajan**
- Inspired by OpenAI API projects and the power of open-source AI tools

---

## 📜 License
MIT License. Feel free to fork, modify, and build upon it.

---

> ⭐ If you like this project, consider starring it on GitHub!
