#------------------------------------------
#
#         TUTORIAL - USER GUIDE
# 
# https://fastapi.tiangolo.com/tutorial/
# 
#------------------------------------------

# pip install "fastapi[standard]"
# fastapi dev main.py
# fastapi run

#------------------------------------------------------
#
#                    FIRST STEP
# 
# https://fastapi.tiangolo.com/tutorial/first-steps/
# 
#------------------------------------------------------

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"Hello": "World"}