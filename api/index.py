from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        prompt = request.form.get('prompt', '')
        file_content = ''

        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                file_content = file.read().decode('utf-8')

        # Combine file content and prompt
        full_prompt = f"{file_content}\n\n{prompt}\n\nBased on the above data and prompt, please provide analysis, solutions, and predictions."

        # Use Gemini API for analysis
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(full_prompt)

        return jsonify({"result": response.text})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

@app.route('/')
def home():
    return "DataFlow Analytics API"