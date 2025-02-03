from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,
                                    index=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str]
    category: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False, default=0.0)
    sku: Mapped[str]

