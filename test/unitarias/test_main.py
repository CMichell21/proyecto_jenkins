import unittest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


class TestSumar(unittest.TestCase):

    def test_suma(self):
        response = client.get("/sumar?a=5&b=3")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["resultado"], 8)


if __name__ == "__main__":
    unittest.main()


##Hola prueba