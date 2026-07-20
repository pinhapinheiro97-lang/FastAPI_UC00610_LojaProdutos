# Lógica da aplicação e negócio

from database import products
from model.product_model import Product


# todos os produtos

def show_products():
    products_list = list(products.find())

    # Converter ObjectId para string
    for product in products_list:
        product["_id"] = str(product["_id"])

    return products_list

#produtos por categoria
def show_product_by_category(categoria: str):
    products_list = list(products.find({"categoria" : categoria}))

    # Converter ObjectId para string
    for product in products_list:
        product["_id"] = str(product["_id"])

    return products_list

#produtos maiores que X   
def show_product_by_stock(minimo: int):
    products_list = list(products.find({"stock" : {"$gte" : minimo}}))

    # Converter ObjectId para string
    for product in products_list:
        product["_id"] = str(product["_id"])

    return products_list

# Criar produto
def create_product(product: Product):
    
    #Converter objeto Pydantic para Dict de forma a inserir no mongodb
    product_dict = product.model_dump()

    #insere no Mongodb
    result = products.insert_one(product_dict)

    #retorna mensagem de sucesso
    return {
        "message": "Produto criado com sucesso",
        "ID": str(result.inserted_id)
    }




# Mostrar produto por caracteristica
def show_product_by_feature(nome: str, valor: str | None = None):
    
    #concatenar strings para aceder ao elemento nested
    campo = f"caracteristicas.{nome}"

    # Se o utilizador apenas indicar o nome da característica
    if valor is None:
        products_list = list(products.find({campo: {"$exists": True}}))

    # Se indicar nome e valor
    else:
        products_list = list(products.find({campo: valor}))

    # Converter ObjectId para string
    for product in products_list:
        product["_id"] = str(product["_id"])

    return products_list
    

