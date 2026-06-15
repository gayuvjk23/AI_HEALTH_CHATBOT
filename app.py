'''from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(
    api_key="AQ.Ab8RN6JbRwfqiaGB4llgn332qazkvoU8gKGG3_ZQQBoio1g8rg"
)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()
    user_message = data.get("message", "")

    prompt = f"""
    You are an AI Healthcare Assistant.

    Rules:
    - Provide general healthcare guidance.
    - Do not diagnose diseases.
    - Do not prescribe medicines.
    - Recommend consulting a doctor for serious symptoms.
    - Keep responses concise and easy to understand.

    User Question:
    {user_message}
    """

    try:
        response = model.generate_content(prompt)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })


if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
"headache": "A headache may be caused by stress, dehydration, lack of sleep, or illness. Drink water, rest, and reduce screen time.",

"fever": "A fever is often a sign that your body is fighting an infection. Stay hydrated and get adequate rest.",

"cough": "A cough may occur due to infections, allergies, or irritation. If it persists for more than two weeks, seek medical advice.",

"cold": "The common cold is a viral infection. Rest, hydration, and proper nutrition can help recovery.",

"sore throat": "A sore throat may be caused by viral infections, allergies, or irritation. Warm fluids may help provide relief.",

"stomach pain": "Stomach pain can result from indigestion, infection, or dietary factors. Monitor symptoms and stay hydrated.",

"nausea": "Nausea may be caused by digestive issues, infections, or motion sickness. Drink fluids and avoid heavy meals.",

"vomiting": "Vomiting can lead to dehydration. Sip water regularly and seek medical advice if symptoms persist.",

"diarrhea": "Diarrhea can cause dehydration. Drink plenty of fluids and consume light foods.",

"constipation": "Increasing fiber intake, drinking water, and regular exercise may help relieve constipation.",

"fatigue": "Fatigue can result from poor sleep, stress, illness, or nutritional deficiencies. Adequate rest is important.",

"stress": "Stress can affect both mental and physical health. Relaxation techniques and regular exercise may help.",

"anxiety": "Anxiety can cause excessive worry and nervousness. Deep breathing and professional support may help.",

"sleep": "Most adults require 7–9 hours of sleep each night for optimal health.",

"insomnia": "Insomnia refers to difficulty falling or staying asleep. Maintaining a consistent sleep schedule may help.",

"back pain": "Back pain may result from poor posture, muscle strain, or injury. Gentle stretching may help.",

"chest pain": "Chest pain should never be ignored. Seek immediate medical attention if symptoms are severe.",

"shortness of breath": "Difficulty breathing can have various causes. Seek medical attention if symptoms are severe or sudden.",

"allergy": "Allergies occur when the immune system reacts to substances such as pollen, dust, or certain foods.",

"asthma": "Asthma affects the airways and may cause wheezing, coughing, and breathing difficulties.",

"dehydration": "Dehydration occurs when the body loses more fluids than it takes in. Drink water regularly.",

"dizziness": "Dizziness may occur due to dehydration, low blood sugar, or other medical conditions.",

"diabetes": "Diabetes is a condition that affects blood sugar levels. Healthy eating and regular monitoring are important.",

"blood pressure": "Maintaining a balanced diet and regular exercise can help manage blood pressure.",

"heart": "Heart health can be improved through exercise, healthy eating, and avoiding smoking.",

"obesity": "Obesity increases the risk of several health conditions. Healthy eating and physical activity can help.",

"weight loss": "Sustainable weight loss is best achieved through a balanced diet and regular exercise.",

"hydration": "Adequate hydration supports overall health and helps regulate body temperature.",

"vitamin d": "Vitamin D supports bone health and immune function.",

"anemia": "Anemia occurs when the body lacks enough healthy red blood cells.",

"immunity": "A healthy immune system is supported by good nutrition, exercise, and sufficient sleep."

}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower()

    for keyword in responses:
        if keyword in user_message:
            return jsonify({
                "reply": responses[keyword]
            })

    return jsonify({
        "reply": "Please consult a healthcare professional for accurate medical advice."
    })

if __name__ == "__main__":
    app.run(debug=True)