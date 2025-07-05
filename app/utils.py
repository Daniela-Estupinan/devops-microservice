import datetime
import logging


def init_logger(name="devops"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def validate_request_data(data, required_fields):
    if not isinstance(data, dict):
        return False
    for field in required_fields:
        if field not in data:
            return False
    return True


def current_timestamp():
    return datetime.datetime.utcnow().isoformat() + "Z"
