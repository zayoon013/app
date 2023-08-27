from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['POST'])
def fetch_website():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is missing'}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        return jsonify({'content': content})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
