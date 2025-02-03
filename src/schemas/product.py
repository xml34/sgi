from pydantic import BaseModel, Field
from typing import Optional


class CreateProductSchema(BaseModel):
    name: str
    description: Optional[str] = Field(default="No description")
    category: str
    price: float
    sku: Optional[str] = Field(default="No description")


class ProductSchemaUpdate(CreateProductSchema):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    sku: Optional[str] = None

    def updation_squema(self):
        result = {}
        for k, v in self.model_dump().items():
            if v is not None:
                result[k] = v
        return result


class ProductSchema(CreateProductSchema):
    id: int

    def creation_squema(self):
        schema = self.model_dump()
        del schema["id"]
        return schema
