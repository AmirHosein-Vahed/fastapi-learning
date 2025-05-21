#----------------------------------------------------------------------
#
#               PATH PARAMETERS AND NUMERIC VALIDATIONS
# 
# https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
# 
#----------------------------------------------------------------------

from typing import Annotated

from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result
# A path parameter is always required as it has to be part of the path.
# Even if you declared it with None or set a default value,
# it would not affect anything, it would still be always required.

