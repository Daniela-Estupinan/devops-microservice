from flask import Flask, request, jsonify
from auth import check_api_key, check_jwt
from utils import validate_request_data, init_logger

app = Flask(__name__)
logger = init_logger()


@app.route('/DevOps', methods=['POST'])
def devops():
    if not check_api_key(request) or not check_jwt(request):
        logger.warning("Unauthorized access attempt.")
        return "ERROR", 403

    data = request.get_json()
    required_fields = ['to', 'message', 'from', 'timeToLifeSec']
    if not validate_request_data(data, required_fields):
        logger.error("Bad request - missing fields.")
        return "ERROR", 400

    to = data['to']
    logger.info(f"Message received for {to}")
    return jsonify({"message": f"Hello {to} your message will be send"})


@app.errorhandler(405)
def method_not_allowed(e):
    return "ERROR", 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
