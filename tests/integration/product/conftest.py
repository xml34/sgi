import pytest
from src.models.product import Product
# from sqlalchemy.ext.asyncio import AsyncSession
# from my_project.database import get_async_session
# from my_project.models import User  # Example model
from src.services.pg_connection import get_db_session
from sqlalchemy import delete
from fastapi.testclient import TestClient
from src.main import app
from unittest import TestCase
from httpx import Response


class ProductTest(TestCase):
    client = TestClient(app)

    def get_product(self, name) -> Response:
        headers = {'Accept': 'application/json'}
        return self.client.get("/product/get?name=%s" % name,
                               headers=headers)
_tester = ProductTest()  # noqa: E305



@pytest.fixture()    # noqa: E303
def clients_ids():
    return list(range(1, 16))


@pytest.fixture()
def pepsi():
    return {
        "name": "pepsi",
        "description": "its a drink",
        "category": "drink",
        "price": 3,
        "sku": "IDK"
    }


@pytest.fixture()
def tester():
    return _tester

#
# @pytest.fixture(scope="function")
# async def preload_data():
#
#     async with get_db_session() as session:
#         async with session.begin():
#             product = Product(
#                 name="Cocacola",
#                 description="its a drink",
#                 category="drink",
#                 price=3,
#                 sku="IDK"
#             )
#             session.add(product)
#
#
# @pytest.fixture(scope="function")
# async def clear_product_table():
#     async with get_db_session() as session:
#         async with session.begin():
#             stmt = delete(Product)
#             session.execute(stmt)
#             session.commit()
#

