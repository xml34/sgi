from fastapi.testclient import TestClient
from src.main import app
from unittest import TestCase


# DB_TEST_URL = "sqlite:///:memory:"


class ProductTest(TestCase):
    client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json().get("message"),
            "Everything is OK   ദ്ദി(>ᴗ•)"
        )

    def test_get_product(self):
        response = self.client.get("/product/get/1")
        assert response.status_code == 404
        # expected_response = {
        #     'category': 'drink',
        #     'description': 'its a drink',
        #     'id': 1,
        #     'name': 'Veneno',
        #     'price': 3,
        #     'sku': "dont know"
        # }
        # self.assertDictEqual(response.json(), expected_response)
