from fastapi.testclient import TestClient
from src.main import app
#from unittest import TestCase

client = TestClient(app)
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("message") == "Everything is OK   ദ്ദി(>ᴗ•) postgresql+asyncpg://sgi:password@localhost:5432/sgi"


def test_health_check2():
    response = client.get("/product/get/1")
    assert response.status_code == 200
    expected_response = {
        'category': 'drink',
        'description': 'its a drink',
        'id': 1,
        'name': 'Veneno',
    }
    #import pdb;pdb.set_trace()
    #TestCase.assertDictEqual("Wrong reponse", response.json(), {})
