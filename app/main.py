from fastapi import FastAPI
import csv

app = FastAPI(title="FastAPI Docker Demo")

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Docker Demo!"}

@app.get("/products")
def get_products():
    products = []
    with open("products.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(row)
    return {"products": products}
