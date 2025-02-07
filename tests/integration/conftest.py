import pytest

import pytest
# from sqlalchemy.ext.asyncio import AsyncSession
# from my_project.database import get_async_session
# from my_project.models import User  # Example model


@pytest.fixture()
def clients_ids():
    return list(range(1, 16))


# @pytest.fixture()
# def mock_context():
#     return build_op_context()
#
#
# @pytest.fixture(scope="function")
# async def preload_data():
#     async with get_async_session() as session:
#         test_user = User(name="Test User", email="test@example.com")
#         session.add(test_user)
#         await session.commit()
