from fastapi.testclient import TestClient
from src.main import app
from unittest import TestCase
from httpx import Response
import time
from remote_pdb import RemotePdb


class ProductTest(TestCase):
    client = TestClient(app)

    def get_product(self, name) -> Response:
        headers = {'Accept': 'application/json'}
        return self.client.get("/product/get?name=%s" % name, headers=headers)

    def test_health_check(self):
        # TODO: move this test to other place
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json().get("message"), "Everything is OK   ദ്ദി(>ᴗ•)"
        )

    def test_01_create_product(self):
        _json = {
            "name": "pepsi",
            "description": "its a drink",
            "category": "drink",
            "price": 3,
            "sku": "IDK"
        }

        response = self.client.post(
            url="/product/create",
            json=_json
        )
        time.sleep(0.2)
        self.assertEqual(response.status_code, 201)
        product = self.get_product("pepsi")
        _json_response = product.json()
        del _json_response["id"]
        self.assertDictEqual(_json_response, _json)

    def test_update_product(self):
        pass
        response = self.client.put("/product/update")
        # get_response = self.get_product()

    def test_delete_product(self):
        pass
        # response = self.client.delete("/product/delete")
        # get_response = self.get_product()
