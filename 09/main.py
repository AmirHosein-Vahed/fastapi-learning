#----------------------------------------------------------------------
#
#               QUERY PARAMETERS AND STRING VALIDATIONS
# 
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
# 
#----------------------------------------------------------------------

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None
):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result
# the default value of q is None, so FastAPI will know it's not required.

# Here we are using Query() because this is a query parameter.
# Later we will see others like Path(), Body(), Header(), and Cookie(),
# that also accept the same arguments as Query().

# in older versions of fastapi (<0.95.0)
async def read_items_2(q: str | None = Query(default=None, max_length=50)):
    pass # The Query version declares q explicitly as being a query parameter.

# You can declare that a parameter can accept None, but that it's still required.
# This would force clients to send a value, even if the value is None.
async def read_items_3(q: Annotated[str | None, Query(min_length=3)]):
    pass

# to declare a query parameter q that can appear multiple times in the URL, you can write:
# http://localhost:8000/multiple?q=foo&q=bar
@app.get('/multiple')
async def read_multiple_query_params(q: Annotated[list[str] | None, Query()] = None):
    query_params = {"q": q}
    return query_params

# You can also define a default list of values if none are provided:
async def read_multiple_query_params_2(q: Annotated[list[str] | None, Query()] = ["Foo", "Bar"]):
    pass


async def read_items_4(
    q: Annotated[
        str | None,
        Query(
            title="Query String",
            description="Query string for the items to search in the database that have a good match",
            min_length=3
        )
    ] = None
):
    pass

# Imagine that you want the parameter to be item-query
# But item-query is not a valid Python variable name.
# The closest would be item_query.
# But you still need it to be exactly item-query...
# Then you can declare an alias, and that alias is what will be used to find the parameter value
# http://127.0.0.1:8000/items/?item-query=foobaritems
async def read_items_5(q: Annotated[str | None, Query(alias="item-query")] = None):
    pass

# You have to leave it there a while because there are clients using it,
# but you want the docs to clearly show it as deprecated.
async def read_items_6(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    pass

# To exclude a query parameter from the generated OpenAPI schema
# (and thus, from the automatic documentation systems),
# set the parameter include_in_schema of Query to False
async def read_items_7(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    pass

# Custom Validation
from pydantic import AfterValidator

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}
def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id
@app.get('/check-id')
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    pass