from pymongo import MongoClient
from bson import ObjectId
from pymongo.collection import Collection

client = MongoClient("mongodb://root:rootpass@localhost:27017/")

db = client['Loja']
products = db.get_collection('Produtos')