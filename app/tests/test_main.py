from app.main import app
from app.auth import generate_jwt

client = app.test_client()
headers = {
    "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
    "X-JWT-KWY": generate_jwt(),
    "Content-Type": "application/json"
}


def test_valid_post():
    response = client.post("/DevOps", json={
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }, headers=headers)
    assert response.status_code == 200
    assert "Juan Perez" in response.get_json()["message"]


def test_invalid_method():
    response = client.get("/DevOps")
    assert response.status_code == 405
    assert response.data == b"ERROR"