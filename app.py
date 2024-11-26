from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import markdown

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyCwzIOji0RwhAmwhQ2E1ZdP-newN-SIJa4")
model = genai.GenerativeModel("gemini-1.5-flash")

def format_response(text):
    formatted_text = f"{text}"
    
    html = markdown.markdown(formatted_text)
    
    return html

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    try:
        response = model.generate_content(user_input)
        formatted_response = format_response(response.text)
        return jsonify({"response": formatted_response})
    except Exception as e:
        error_message = f"## Error\n\nAn error occurred: {str(e)}"
        formatted_error = format_response(error_message)
        return jsonify({"error": formatted_error}), 500

if __name__ == '__main__':
    app.run(debug=True)

