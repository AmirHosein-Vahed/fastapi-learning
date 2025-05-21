#---------------------------------------------------------------
#
#                 BODY - MULTIPLE PARAMETERS
# 
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/
# 
#---------------------------------------------------------------

from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put('/items/{item_id}')
async def update_item(
    item_id: Annotated[int, Path(title="ID of item", ge=0, le=1000)],
    importance: Annotated[int, Body()],
    q: str | None = None,
    item: Item | None = None,
    user: User | None = None,
):
    result = {"item_id": item_id, "importance": importance}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})
    if user:
        result.update({"user": user})
    return result

# for embeding body
@app.post('/items/')
async def create_item(
    item: Annotated[Item, Body(embed=True)]
):
    return {"item": item}
# By default, FastAPI will then expect its body directly.
# But if you want it to expect a JSON with a key item and inside of it the model contents,
# as it does when you declare extra body parameters, you can use the special Body parameter embed=True