# -------------------------------------------------------
#
#                    EXTRA MODELS
#
# https://fastapi.tiangolo.com/tutorial/extra-models/
#
# -------------------------------------------------------

# This is especially the case for user models, because:
    # The input model needs to be able to have a password.
    # The output model should not have a password.
    # The database model would probably need to have a hashed password.

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "secret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("user saved! ...not reqlly.")
    return user_in_db

@app.post('/users/', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# --------------------------------------------------------------------------------

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type: str = 'car'

class PlaneItem(BaseItem):
    type: str = 'plane'
    size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {"description": "Music is my aeroplane", "type": "plane", "size": 5}
}

@app.get('/items/{item_id}', response_model=PlaneItem | CarItem)
async def read_item(item_id: str):
    return items[item_id]

@app.get('/cars/', response_model=list[CarItem])
async def read_cars():
    return [
        {"description": "description 1", "type": "car"},
        {"description": "description 2", "type": "car"},
        {"description": "description 3", "type": "car"},
        {"description": "description 4", "type": "car"},
    ]

# -----------------------------------------------------------------------------------

@app.get('/key-weights/', response_model=dict[str, float])
async def read_key_weights():
    return {"foo": 2.3, "bar": 3.4}