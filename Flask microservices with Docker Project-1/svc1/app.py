from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/trigger', methods=['GET'])
def trigger():
    payload = {'a': 10, 'b': 20}
    try:
        response = requests.post('http://svc2:8001/calculate', json=payload)
        return jsonify({
            "svc2_response": response.json()
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
