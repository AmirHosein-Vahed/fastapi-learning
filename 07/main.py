#------------------------------------------------------
#
#                    QUERY PARAMS
# 
# https://fastapi.tiangolo.com/tutorial/query-params/
# 
#------------------------------------------------------

# When you declare other function parameters that are not part of the path parameters,
# they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"},
                 {"item_name": "Booz"}
                ]
@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get('/items/{item_id}')
async def read_item_detail(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
# Also notice that FastAPI is smart enough to notice that
# the path parameter item_id is a path parameter and q, short are not, so, it's a query parameter.
# (short = true, on, 1, True, yes) == (short = True)

@app.get('/users/{user_id}/orders/{order_id}')
async def read_user_order(
    user_id: int,
    order_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {"order_id": order_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# Required query parameters
@app.get('/test')
async def read_test(needy: str):
    return {"needy": needy}

# item_id: str, needy: str, skip: int = 0, limit: int | None = None
# item_id => path params
# needy   => required query params
# skip    => query params with default value
# limit   => entirely optional query params

from enum import Enum

class Size(str, Enum):
    small   = "s"
    medium  = "m"
    large   = "l"
    xlarge  = "xl"
    xxlarge = "xxl"

# You could also use Enums the same way as with path params
@app.get('/tshirt')
async def read_size(size: Size):
    return {"size": size}