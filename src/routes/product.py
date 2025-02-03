from fastapi import APIRouter, Depends

from src.schemas.product import (
    ProductSchemaUpdate, CreateProductSchema
)
from src.services.product import ProductService
from src.models.product import Product


def init_product_router():
    router = APIRouter(prefix="/product", tags=["Product"])

    @router.get(
        path="/get/{product_id}",
        description="Returns a single product",
        name="Get Product",
    )
    async def get_product(
        product_id: int,
        service: ProductService = Depends()
    ):
        product = await service.get(product_id)
        return product

    @router.post(
        path="/create",
        description="Create Product",
        name="Create Product"
    )
    async def create_product(
            request: CreateProductSchema = Depends(),
            service: ProductService = Depends()
    ):
        new_product = Product(**request.model_dump())
        await service.create(new_product)
        return {"message": "%s Created successfully" % new_product.name}

    @router.put(
        path="/update/{product_id}",
        description="Update Product",
        name="Update Product"
    )
    async def update_product(
            request: ProductSchemaUpdate = Depends(),
            service: ProductService = Depends()
    ):
        response: str = await service.update(request)
        return {"message": "%s. %s" % (request.name, response)}

    return router
