# Inserção de dados para popular a DB

# nome, preço, categoria, stock e caracteristicas
# carregados 3 tipos de produto - Informatica, Roupa e Musica

from database import products



'''
products.insert_one({
    "nome": "Computador",
    "preco": 499.0,
    "categoria": "Informática",
    "stock": 2,
    "caracteristicas":{"marca": "Lenovo", "memória": "16GB", "cor": "cinzento"}
    })
'''


products.insert_many([
    {
    "nome": "Camisola",
    "preco": 25.0,
    "categoria": "Roupa",
    "stock": 12,
    "caracteristicas":{"tamanho": "M", "cor": "azul", "material": "algodão"}    
    },
    {
    "nome": "Camisa",
    "preco": 25.0,
    "categoria": "Roupa",
    "stock": 12,
    "caracteristicas":{"tamanho": "S", "cor": "salmão", "material": "algodão"}    
    },
    {
    "nome": "Sweat shirt",
    "preco": 40.0,
    "categoria": "Roupa",
    "stock": 7,
    "caracteristicas":{"tamanho": "L", "cor": "preto", "material": "lã"}
    },
    {
    "nome": "Calções",
    "preco": 54.0,
    "categoria": "Roupa",
    "stock": 2,
    "caracteristicas":{"tamanho": "S", "cor": "azul", "material": "ganga"}
    },
    {
    "nome": "Calças",
    "preco": 90.0,
    "categoria": "Roupa",
    "stock": 12,
    "caracteristicas":{"tamanho": "L", "cor": "azul", "material": "ganga"}
    },
    {
    "nome": "Disco rigido",
    "preco": 110.0,
    "categoria": "Informática",
    "stock": 25,
    "caracteristicas":{"marca": "Toshiba", "memória": "1TB", "cor": "preto"}
    },
    {
    "nome": "Fones",
    "preco": 89.0,
    "categoria": "Informática",
    "stock": 10,
    "caracteristicas":{"marca": "Sony", "tipo de ligação": "sem fios", "cor": "rosa"}
    },
    {
    "nome": "Auriculares",
    "preco": 12.0,
    "categoria": "Informática",
    "stock": 5,
    "caracteristicas":{"marca": "Samsung", "tipo de ligação": "com fios", "cor": "branco"}
    },
    {
    "nome": "Guitarra Elétrica",
    "preco": 420.0,
    "categoria": "Música",
    "stock": 3,
    "caracteristicas":{"marca": "Fender", "construção": "maple", "cor": "vermelho"}
    },
    {
    "nome": "Guitarra Acústica",
    "preco": 359.0,
    "categoria": "Música",
    "stock": 9,
    "caracteristicas":{"marca": "Ashton", "construção": "rosewood", "cor": "castanho"}
    },
    {
    "nome": "Sintetizador",
    "preco": 1099.0,
    "categoria": "Música",
    "stock": 7,
    "caracteristicas":{"marca": "Yamaha", "construção": "aluminio", "cor": "cinzento"}
    },
    {
    "nome": "Baixo Elétrico",
    "preco": 786.0,
    "categoria": "Música",
    "stock": 10,
    "caracteristicas":{"marca": "Gibson", "construção": "darkwood", "cor": "sunburn"}
    }])






