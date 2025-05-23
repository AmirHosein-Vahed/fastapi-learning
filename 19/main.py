#------------------------------------------------------------
#
#                   COOKIE PARAMETER MODELS
# 
# https://fastapi.tiangolo.com/tutorial/cookie-param-models/
# 
#------------------------------------------------------------

# This is supported since FastAPI version 0.115.0

from typing import Annotated

from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()

class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

@app.get('/items/')
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies