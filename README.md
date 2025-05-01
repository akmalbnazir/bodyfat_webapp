# 🧠 AI Body Fat Estimator

This is an AI-powered web app that estimates a user's **body fat percentage** based on a torso image and biometric data. Powered by **OpenAI GPT-4.1**, it performs visual analysis and returns structured health insights.

> Built with **Flask**, styled with **Tailwind CSS**, and deployable via **Replit** or any web host.

---

## ✨ Features

- 📸 Upload image (full torso, good lighting)
- 🧍 Enter height, weight, age, and gender
- 🤖 GPT-4.1 analyzes body shape, muscle definition, and fat distribution
- 📊 Outputs estimated **body fat %** with explanation and fitness category
- 🧠 Markdown-rendered analysis result with confidence level and health tips

---

## 🔧 Installation (Local Dev)

### 1. Clone the repo

```bash
git clone https://github.com/akmalbnazir/bodyfat_webapp.git
cd bodyfat_webapp
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate         # For Windows
# OR
source venv/bin/activate      # For macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a file called `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> This file is ignored via `.gitignore` and must not be committed.

### 5. Run the app

```bash
python app.py
```

Then open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🚀 Replit Deployment

1. Go to [https://replit.com](https://replit.com)
2. Import this repo from GitHub
3. Add your `OPENAI_API_KEY` to Replit Secrets
4. Hit **Run** and your app will be publicly accessible!

You can also add a `.replit` file:

```ini
run = "python app.py"
```

---

## 🛡 License

**MIT License**  
Use this app for educational or personal fitness tracking. Do not use it for medical diagnosis or body shaming.

---

## 🙌 Final Notes

Built with ❤️ by **Akmal Nazir**
