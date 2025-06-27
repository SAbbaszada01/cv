from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_cv', methods=['POST'])
def create_cv():
    user_data = request.json.get('data')
    prompt = f"CV üçün məlumat: {user_data}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"cv": response["choices"][0]["message"]["content"]})

if __name__ == '__main__':
    app.run(debug=True)

