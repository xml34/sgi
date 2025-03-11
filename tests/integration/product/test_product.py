import time
from .conftest import ProductTest
from httpx import Response



def test_health_check(tester):  # noqa: E303
    # TODO: move this test to other place
    response = tester.client.get("/health")
    tester.assertEqual(response.status_code, 200)
    tester.assertEqual(
        response.json().get("message"), "Everything is OK   ദ്ദി(>ᴗ•)"
    )


def test_01_create_product(tester: ProductTest, pepsi: dict):
    _json = pepsi

    response: Response = tester.client.post(
        url="/product/create",
        json=_json
    )

    time.sleep(0.1)
    tester.assertEqual(response.status_code, 201)
    product: Response = tester.get_product("pepsi")
    _json_response = product.json()
    del _json_response["id"]
    tester.assertDictEqual(_json_response, _json)


def test_02_update_product(tester: ProductTest, pepsi: dict):
    pass
    # _pepsi: Response = tester.get_product(pepsi.get("name"))
    # tester.assertEqual(_pepsi.status_code, 200)
    #
    # tester.client.put(
    #     "/product/update/%d" % _pepsi.json()["id"],
    #     json={"price": 4}
    # )
    #
    # time.sleep(0.1)
    #
    # _pepsi: Response = tester.get_product(pepsi.get("name"))
    # tester.assertEqual(_pepsi.status_code, 200)
    # tester.assertEqual(_pepsi.json()["prise"], 4)
    # get_response = self.get_product()


def test_delete_product():
    pass
    # response = self.client.delete("/product/delete")
    # get_response = self.get_product()
