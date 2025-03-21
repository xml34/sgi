from sqlalchemy.orm import declarative_base


Base = declarative_base()

from .product import Product  # noqa: E402, F401
