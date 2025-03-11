from sqlalchemy.ext.asyncio import AsyncSession
from src.services.pg_connection import get_db_session
from fastapi import Depends, HTTPException
from sqlalchemy import select, update, delete
from src.models import Product
from src.schemas.product import ProductSchemaUpdate


class ProductService:
    db: AsyncSession = None

    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def get(self, id_: int) -> Product:
        async with self.db as session:
            async with session.begin():
                result = await session.execute(select(Product).filter(Product.id == id_))
                product = result.scalar_one_or_none()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        return product

    async def get_by_name(self, name: str) -> Product:
        async with self.db as session:
            async with session.begin():
                result = await session.execute(select(Product).filter(Product.name == name))
                product = result.scalar_one_or_none()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        return product

    async def exists(self, name: str) -> bool:
        async with self.db as session:
            async with session.begin():
                result = await session.execute(
                    select(Product).filter(Product.name == name))
                product = result.scalar_one_or_none()

        return product is not None

    async def create(self, product: Product) -> None:
        if await self.exists(product.name):
            raise HTTPException(
                status_code=400,
                detail="Product with name %s already exists" % product.name
            )

        async with self.db as session:
            async with session.begin():
                session.add(product)

    async def update(self, product_id: int,  product: ProductSchemaUpdate) -> str:
        if product.updation_squema():
            async with self.db as session:
                async with session.begin():
                    await session.execute(
                        update(Product).where(
                            Product.id == product_id).values(
                            **product.updation_squema())
                    )
            return "Product successfully updated"
        return "Updated with no changes"

    async def delete(self, product_id) -> str:
        async with self.db as session:
            async with session.begin():
                await session.execute(
                    delete(Product).where(Product.id == product_id)
                )
        return "Product successfully updated"
