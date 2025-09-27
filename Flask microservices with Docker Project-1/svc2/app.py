from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if a is None or b is None:
        return jsonify({"error": "Missing 'a' or 'b'"}), 400

    result = a + b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
