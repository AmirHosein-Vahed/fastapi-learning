#-------------------------------------------------------
#
#                    COOKIE PARAMETERS
# 
# https://fastapi.tiangolo.com/tutorial/cookie-params/
# 
#-------------------------------------------------------

from typing import Annotated

from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get('/items/')
async def read_items(ads_in: Annotated[str | None, Cookie()] = None):
    return {"ads_in": ads_in}