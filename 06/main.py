#------------------------------------------------------
#
#                    PATH PARAMS
# 
# https://fastapi.tiangolo.com/tutorial/path-params/
# 
#------------------------------------------------------

from fastapi import FastAPI

app = FastAPI()

@app.get('/items1/{item_id}')
async def read_root(item_id):
    return {"item_id": item_id}

@app.get('/items2/{item_id}')
async def read_root(item_id: int):
    return {"item_id": item_id}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet   = "lenet"

@app.get('/models/{model_name}')
async def read_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path}