from fastapi import FastAPI
from model import products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome to fastapi"}

product_list = [
    products(id=1, name="phone", description="a good phone", price=989, quantity=10),
    products(id=2, name="phone", description="a good phone", price=959, quantity=50),
    products(id=5, name="phone", description="a good phone", price=959, quantity=50),
    products(id=8, name="phone", description="a good phone", price=959, quantity=50)
]

# GET ALL PRODUCTS
@app.get("/products")
def get_all_products():
    return product_list

# GET PRODUCT BY ID
@app.get("/products/{id}")
def get_product(id: int):
    for product in product_list:
        if product.id == id:
            return product

    return {"message": "product not found"}

# CREATE PRODUCT
@app.post("/products")
def create_product(product: products):
    product_list.append(product)
    return {"message": "product added successfully"}

# UPDATE PRODUCT
@app.put("/products/{id}")
def update_product(id: int, updated_product: products):

    for index, product in enumerate(product_list):
        if product.id == id:
            product_list[index] = updated_product
            return {"message": "product updated successfully"}

    return {"message": "product not found"}

# DELETE PRODUCT
@app.delete("/products/{id}")
def delete_product(id: int):

    for product in product_list:
        if product.id == id:
            product_list.remove(product)
            return {"message": "product deleted successfully"}

    return {"message": "product not found"}

# COUNT PRODUCTS
@app.get("/products/count")
def product_count():
    return {"total_products": len(product_list)}