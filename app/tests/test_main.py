import unittest
from app.main import app
from app.auth import generate_jwt


class DevOpsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.headers = {
            "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
            "X-JWT-KWY": generate_jwt(),
            "Content-Type": "application/json"
        }

    def test_valid_post(self):
        response = self.client.post(
            "/DevOps",
            json={
                "message": "This is a test",
                "to": "Juan Perez",
                "from": "Rita Asturia",
                "timeToLifeSec": 45,
            },
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Juan Perez", response.get_json()["message"])

    def test_invalid_method(self):
        response = self.client.get("/DevOps")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data, b"ERROR")


if __name__ == "__main__":
    unittest.main()
