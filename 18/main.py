#-------------------------------------------------------
#
#                    HEADER PARAMETERS
# 
# https://fastapi.tiangolo.com/tutorial/header-params/
# 
#-------------------------------------------------------

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()

@app.get('/items/')
async def read_items(user_agent: Annotated[str| None, Header()] = None):
    return {"User-Agent": user_agent}
# by default, Header will convert the parameter names characters
# from underscore (_) to hyphen (-)to extract and document the headers.
# HTTP headers are case-insensitive

@app.get('/orders/')
async def read_orders(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token": x_token}