#----------------------------------------------
#
#                 REQUEST BODY
# 
# https://fastapi.tiangolo.com/tutorial/body/
# 
#----------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# @app.post('/items/')
# async def create_item(item: Item):
#     return item
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Request body + path params + query params
# You can also declare body, path and query parameters, all at the same time.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# If the parameter is declared to be of the type of a Pydantic model,
# it will be interpreted as a request body.