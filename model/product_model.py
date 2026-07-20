from pydantic import BaseModel, Field

class Product(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(gt=0)
    categoria: str = Field(min_length=1)
    stock: int = Field(ge=0)
    caracteristicas: dict[str, str | int]
