# -------------------------------------------------------
#
#               RESPONSE MODEL - RETURN TYPE
#
# https://fastapi.tiangolo.com/tutorial/response-model/
#
# -------------------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 0.5
    tags: list[str] = []


# @app.post('/items/')
# async def create_item(item: Item) -> Item:
#     return item

# @app.get('/items/')
# async def read_items() -> list[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="plumbus", price=32.0)
#     ]


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/items/", response_model=list[Item])
async def read_items():
    return [Item(name="Portal Gun", price=42.0), Item(name="plumbus", price=32.0)]


# ---------------------------------------------------------------------------------


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


# Don't do this in production!
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


# ---------------------------------------------------------------------------------


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInn(BaseUser):
    password: str


# @app.post('/users2/')
# async def create_user2(user: UserIn) -> BaseUser:
#     return user


@app.post("/users2/", response_model=BaseUser)
async def create_user2(user: UserInn):
    return user


# ---------------------------------------------------------------------------------

from fastapi import Response
from fastapi.responses import RedirectResponse, JSONResponse


@app.get("/portal/")
async def read_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.google.com")
    return JSONResponse(content={"msg": "here is portal."})


# ---------------------------------------------------------------------------------

# if you had something like a union between different types
# where one or more of them are not valid Pydantic types, for example this would fail:
# @app.get("/portal2/")
# async def read_portal2(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}


# Continuing from the example above, you might not want to have
# the default data validation, documentation, filtering, etc. that is performed by FastAPI.
@app.get("/portal3/", response_model=None)
async def read_portal3(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}


# ---------------------------------------------------------------------------------

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
)
async def read_item(item_id: str):
    return items[item_id]


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]
