from src.config import settings
from typing import AsyncIterator, Any
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker)
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, AsyncConnection

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#preventing-implicit-io-when-using-asyncsession
    __mapper_args__ = {"eager_defaults": True}


class DatabaseSessionManager:
    _engine: AsyncEngine | None = None
    _session_maker: async_sessionmaker[AsyncSession] | None = None

    def __init__(self, host, engine_kwargs: dict[str: Any] = None) -> None:

        if engine_kwargs is None:
            engine_kwargs = {}

        self._engine = create_async_engine(host, **engine_kwargs)
        self._session_maker = async_sessionmaker(
            autocommit=False, bind=self._engine, expire_on_commit=False
        )

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._session_maker = None

    @asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine in None:
            raise Exception("DatabaseSessionManager is no initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._session_maker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._session_maker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    def is_engine_none(self) -> bool:
        if self._engine is None:
            return True
        return False


session_manager = DatabaseSessionManager(
    host=settings.database_url,
    engine_kwargs={"echo": settings.echo_sql}
)


async def get_db_session():
    async with session_manager.session() as session:
        yield session





