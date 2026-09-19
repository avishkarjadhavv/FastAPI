from fastapi import FastAPI
from getData import products
from py_dantic import ProductDTO

aj = FastAPI()

@aj.get("/get_product")
def get_product1():
    return products


@aj.delete("/delete_product/{product_id}")
def remove_product(product_id : int):
    for index , oneProduct in enumerate(products):
        if(oneProduct.get("id")==product_id):
            deleted_product = products.pop(index)
            return f"Product with id {product_id} is deleted successfully..."

    return f"Product not found with id {product_id}"
