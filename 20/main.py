#-------------------------------------------------------------
#
#                   HEADER PARAMETER MODELS
# 
# https://fastapi.tiangolo.com/tutorial/header-param-models/
# 
#-------------------------------------------------------------

# This is supported since FastAPI version 0.115.0

from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get('/items/')
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers