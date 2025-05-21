#-------------------------------------------------------------
#
#                  Query Parameter Models
# 
# https://fastapi.tiangolo.com/tutorial/query-param-models/
# 
#-------------------------------------------------------------

# This is supported since FastAPI version 0.115.0

from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    # restrict the query parameters that you want to receive

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get('/items/')
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
# http://127.0.0.1:8000/items/?limit=50&offset=10&order_by=created_at&tags=a&tags=b
