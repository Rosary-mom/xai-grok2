import os
from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # Load .env file for API key

app = Flask(__name__)
CORS(app)  # Allow cross-origin for frontend

# Initialize xAI client (OpenAI-compatible)
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),  # Add your key to .env as XAI_API_KEY=your_key_here
    base_url="https://api.x.ai/v1"
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    model = data.get('model', 'grok-beta')  # Default to a public model; change to 'grok-4' or 'grok-4-beta' if subscribed

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for COP30 scenarios and rosary-related queries."},  # Customize prompt
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,  # Adjust as needed
            temperature=0.7
        )
        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run on localhost:5000
