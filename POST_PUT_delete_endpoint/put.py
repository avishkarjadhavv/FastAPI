from fastapi import FastAPI
from getData import products
from py_dantic import ProductDTO


aj = FastAPI()

@aj.get("/get_product")
def getProduct():
    return products

@aj.put("/update_product/{product_id}")
def update_data(put_data : ProductDTO , product_id : int):
    for index , oneProduct in enumerate(products):
        if(oneProduct.get("id") == product_id):
            products[index] = put_data.model_dump()
            return "Data updated successfully"

    return f"Data not found with id {product_id}"

    
    