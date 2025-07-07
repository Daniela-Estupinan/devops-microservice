from flask import Flask, request, jsonify
from auth import check_api_key, check_jwt
from metrics import metrics

app = Flask(__name__)


@app.route('/DevOps', methods=['POST'])
def devops():
    if not check_api_key(request) or not check_jwt(request):
        return "ERROR", 403

    data = request.get_json()
    if not data or 'to' not in data:
        return "ERROR", 400

    to = data['to']
    return jsonify({"message": f"Hello {to} your message will be send"})


@app.route('/metrics')
def prometheus_metrics():
    return metrics()


@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


@app.errorhandler(405)
def method_not_allowed(e):
    return "ERROR", 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
