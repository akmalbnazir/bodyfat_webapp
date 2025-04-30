import os
import base64
from flask import Flask, render_template, request
from PIL import Image
import openai

openai.api_key = "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"

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_body_fat_estimate(image_path, height, weight, age, gender):
    base64_image = encode_image_to_base64(image_path)

    prompt = f"""
You are an AI health and fitness analyst. The image shows a user's upper body, and the following metadata is provided:

- Height: {height} cm
- Weight: {weight} kg
- Age: {age}
- Gender: {gender.capitalize()}

Your job is to estimate the user's **body fat percentage** and return your results in the following structured format.

---

**🧮 Estimated Body Fat Percentage:**
- Return a number or range (e.g. “10% to 13%”) based on the image and metadata.

---

**📌 Visual Indicators Observed:**
- Abdominal Definition: [your analysis]
- Oblique Visibility: [your analysis]
- Chest & Pectorals: [your analysis]
- Upper Arms & Shoulders: [your analysis]
- Vascularity & Muscle Lines: [your analysis]
- Hip/Love Handles: [your analysis]

---

**📊 User Metadata:**
- Height: {height} cm
- Weight: {weight} kg
- Age: {age}
- Gender: {gender.capitalize()}

---

**✅ Confidence Level:**
- State your confidence level (e.g. "High Confidence") and explain why the visual indicators support your estimate.

---

**📚 Interpretation & Explanation:**
- Briefly explain what the visual indicators mean in terms of body fat classification and athletic level.
- Compare the user to general population standards or athlete categories.

---

**🧩 Matching Body Fat Range Category:**
- Match the user to one of these categories:
    - 6-9%: Extreme Definition (e.g., bodybuilders)
    - 10-13%: Athletic, Visible Abs, Muscle Definition
    - 14-17%: Average Fit
    - 18-22%: Mild Muscle Visibility, Higher Fat
    - 23%+: Overweight

---

**📝 Final Recommendation or Notes:**
- Give fitness tips, guidance, or health advice if needed. Mention if DEXA or caliper scans are recommended for more accuracy.
"""


    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        max_tokens=800
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        height = request.form["height"]
        weight = request.form["weight"]
        age = request.form["age"]
        gender = request.form["gender"]

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            result = get_body_fat_estimate(filepath, height, weight, age, gender)
            os.remove(filepath)
            return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
