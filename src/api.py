from fastapi import FastAPI
from src.routes import product, default
from src.services.pg_connection import session_manager
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """

    yield
    if not session_manager.is_engine_none:
        await session_manager.close()  # Close Db connection


def init_api() -> FastAPI:
    app = FastAPI(title="My SGI Project", lifespan=lifespan)
    _include_routes(app)
    return app


def _include_routes(app: FastAPI) -> None:
    app.include_router(default.router)
    app.include_router(product.init_product_router())
