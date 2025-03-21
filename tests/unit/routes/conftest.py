import pytest
from fastapi.testclient import TestClient
from src.main import app
from unittest import TestCase
from httpx import Response
from unittest.mock import AsyncMock
from src.models.product import Product


class ProductTest(TestCase):
    client = TestClient(app)

    def get_product(self, name) -> Response:
        headers = {'Accept': 'application/json'}
        return self.client.get("/product/get?name=%s" % name,
                               headers=headers)
_tester = ProductTest()  # noqa: E305


@pytest.fixture()
def tester():
    return _tester


@pytest.fixture
def mock_db_session():
    """Mock database session"""
    session = AsyncMock()
    return session


@pytest.fixture
def cocacola_example():
    """Mock database session"""
    return Product(
        id=1,
        name="Cocacola",
        description="its a drink",
        category="drink",
        price=3,
        sku="IDK"
    )

@pytest.fixture
def cocacola_response():
    """Mock database session"""
    return {
        "id": 1,
        "name": "Cocacola",
        "description": "its a drink",
        "category": "drink",
        "price": 3,
        "sku": "IDK"

    }
