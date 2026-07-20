from database import products

resultado = list(products.find({
    "caracteristicas.marca": "Sony"
}))

print(resultado)