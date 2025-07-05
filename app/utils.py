data = request.get_json()
if not validate_request_data(data, ['to', 'message', 'from', 'timeToLifeSec']):
    logger.error("Bad request - missing fields.")
    return "ERROR", 400

to = data['to']
logger.info(f"Message received for {to}")
return jsonify({"message": f"Hello {to} your message will be send"})
