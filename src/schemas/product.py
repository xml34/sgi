from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Body


class CreateProductSchema(BaseModel):
    name: str = Field(Body(default="No description"))
    description: Optional[str] = Field(Body(default="No description"))
    category: str = Field(Body(default="No description"))
    price: float = Field(Body(default="No description"))
    sku: Optional[str] = Field(Body(default="No description"))


class ProductSchemaUpdate(CreateProductSchema):
    id: int = Field(Body(default="No description"))
    name: Optional[str] = Field(Body(default="No description"))
    description: Optional[str] = Field(Body(default="No description"))
    category: Optional[str] = Field(Body(default="No description"))
    price: Optional[float] = Field(Body(default="No description"))
    sku: Optional[str] = Field(Body(default="No description"))

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
