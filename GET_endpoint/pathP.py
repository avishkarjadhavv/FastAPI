from fastapi import FastAPI
from getData import products

aj = FastAPI()

@aj.get("/")
def greet():
    return "welcome to AJ's LocalHost"

@aj.get("/products")
def get_products():
    return products

@aj.get("/product/{product_id}")
def get_one_product(product_id:int):
    for oneProduct in products:
        if(oneProduct.get("id") == product_id):
            return oneProduct

    return f"Product not found with id {product_id}"