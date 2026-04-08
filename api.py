from fastapi import FastAPI

app = FastAPI()

# временное хранилище
items = []


@app.get("/")
def read_root():
    return {"message": "API is working"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def add_item(item: dict):
    items.append(item)
    return {"message": "Item added", "item": item}