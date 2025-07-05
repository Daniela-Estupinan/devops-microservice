import jwt

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "supersecretkey"

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