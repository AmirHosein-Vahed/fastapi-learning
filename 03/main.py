#--------------------------------------
#
#    CONCURRENCY AND ASYNC/AWAIT
# 
# https://fastapi.tiangolo.com/async/
# 
#--------------------------------------

from fastapi import FastAPI

app = FastAPI()

# If you are using third party libraries that tell you to call them with `await`, like:
@app.get('/')
async def read_result():
    result = await some_library()
    return result 
# If you are using a third party library that communicates with something (a database, an API, the file system, etc.)
# and doesn't have support for using await, (this is currently the case for most database libraries),
# then declare your path operation functions as normally, with just def, like:
@app.get('/')
def read_result():
    result = some_library()
    return result 

async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers
@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers