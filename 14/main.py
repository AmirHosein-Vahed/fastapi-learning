#------------------------------------------------------------
#
#                   BODY - NESTED MODELS
# 
# https://fastapi.tiangolo.com/tutorial/body-nested-models/
# 
#------------------------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price:float
    tax: float | None = None
    tags: set[str] = set()
    # tags: list[str] = []
    image: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.put('/items/{item_id}/')
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, "item": item}
    return result

@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer

@app.post('/images/multiple/')
async def create_multiple_images(images: list[Image]):
    return images

@app.post('/index-weight/')
async def create_index_weights(weights: dict[int, float]):
    return weights
# JSON only supports str as keys.
# But Pydantic has automatic data conversion.
# This means that, even though your API clients can only send strings as keys,
# as long as those strings contain pure integers, Pydantic will convert them and validate them.
# And the dict you receive as weights will actually have int keys and float values.