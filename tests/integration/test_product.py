from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from fastapi.testclient import TestClient
import pytest


@pytest.mark.asyncio
async def test_my_crud_function(
        db_session: AsyncSession,
        client: TestClient,
        setup_database
):
    response = client.get("/product/get/1")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"name": "Foo", "description": "A test item"}
