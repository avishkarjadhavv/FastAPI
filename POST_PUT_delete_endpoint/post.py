from fastapi import FastAPI
from getData import products
from py_dantic import ProductDTO


aj = FastAPI()

@aj.get("/get_product")
def getProduct():
    return products

@aj.post("/create_product")
def create_product(post_data : ProductDTO):
    products.append(post_data)
    return {"Status" : "Product Created Successfully..."}