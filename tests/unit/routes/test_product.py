import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.services.product import ProductService

client = TestClient(app)


def dependency_overrider(function):
    def wrapper(*args: list[object]):
        for dependency in args:
            app.dependency_overrides[dependency]

        function(*args)

        for dependency in args:
            del app.dependency_overrides[dependency]
    return wrapper


@pytest.mark.asyncio
def test_health_check(tester):  # noqa: E303
    # TODO: move this test to other place
    response = tester.client.get("/health")
    tester.assertEqual(response.status_code, 200)
    tester.assertEqual(
        response.json().get("message"), "Everything is OK   ദ്ദി(>ᴗ•)"
    )


def test_get_product_success(
        tester, mock_db_session, cocacola_example, cocacola_response):
    mock_db_session.get.return_value = cocacola_example
    app.dependency_overrides[ProductService] = lambda: mock_db_session
    response = tester.client.get("product/get/1")
    tester.assertEqual(response.status_code, 200)
    tester.assertDictEqual(response.json(), cocacola_response)
    del app.dependency_overrides[ProductService]
