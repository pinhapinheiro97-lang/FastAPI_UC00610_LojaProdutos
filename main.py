from fastapi import FastAPI
from faker import Faker
from routes.products import *


fake = Faker(locale='pt_PT')

# inicializar API
app = FastAPI()

#Incluir endpoints
app.include_router(router)