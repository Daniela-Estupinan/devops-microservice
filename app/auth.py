import jwt
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")
JWT_SECRET = os.getenv("JWT_SECRET")


def check_api_key(req):
    return req.headers.get("X-Parse-REST-API-Key") == API_KEY


def check_jwt(req):
    token = req.headers.get("X-JWT-KWY")
    try:
        jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return True
    except Exception:
        return False


def generate_jwt():
    return jwt.encode({"user": "devops"}, JWT_SECRET, algorithm="HS256")
