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
        name="Get Product"
    )
    async def get_product(
        product_id: int,
        service: ProductService = Depends()
    ):
        product = await service.get(product_id)
        return product

    @router.get(
        path="/get",
        description="Returns a single product",
        name="Get Product"
    )
    async def get_product(
            name: str,
            service: ProductService = Depends()
    ):
        product = await service.get_by_name(name)
        return product

    @router.post(
        path="/create",
        description="Create Product",
        name="Create Product",
        status_code=201
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
            product_id,
            request: ProductSchemaUpdate = Depends(),
            service: ProductService = Depends()
    ):
        response: str = await service.update(
            product_id=product_id, product=request
        )
        return {"message": "%s. %s" % (request.name, response)}

    @router.delete(
        path="/delete/{product_id}",
        description="Deletes a single product",
        name="Get Product"
    )
    async def delete_product(
        product_id: int,
        service: ProductService = Depends()
    ):
        return await service.delete(product_id)

    return router
