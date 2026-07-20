from fastapi import APIRouter
from services import product_service
from model.product_model import Product

#inicia o router para as rotas
router = APIRouter()


# backend first page
@router.get('/')
async def root():
    return {"message": "Loja Produtos API dá as boas vindas"}

#Retornar todos os produtos
@router.get('/produtos')
async def get_products():
    return product_service.show_products()


#Retornar todos os produtos de uma categoria
@router.get('/produtos/categoria/{categoria}')
async def get_products_by_category(categoria: str):
    return product_service.show_product_by_category(categoria)


#Retornar os produtos maiores que o stock colocado /stock?minimo=x
@router.get('/produtos/stock')
async def get_products_by_stock(minimo: int):
    return product_service.show_product_by_stock(minimo)

#Criar produto
@router.post('/produtos')
async def create_product(product : Product):
    return product_service.create_product(product)


#retornar produtos com determinada caracteristica
@router.get('/produtos/caracteristicas')
async def get_product_by_caracteristicas(
    nome : str,
    valor : str | None = None
    ):
        return product_service.show_product_by_feature(nome, valor)




