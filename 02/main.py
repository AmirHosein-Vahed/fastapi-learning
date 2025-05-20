#---------------------------------------------
#
#               PYTHON TYPES
# 
# https://fastapi.tiangolo.com/python-types/
# 
#----------------------------------------------

from typing import Union, Optional

name: str     = "ali"
age: int      = 22
height: float = 178.4

a: list[str] = ["a", "b", "c"]
b: list[int] = [12, 13, 24]

c: tuple[int, str, int] = (12, "good", 19)
d: set[bytes]           = {bytes(10), bytes(38), bytes(244)}
e: dict[str, float]     = {"ali": 19.8}

f: list[dict[str, int]] = [{"ali": 19.8}, {"hasan": 17.4}, {"gholi": 15.2}]

g: int | str = 10
g: int | str = "hello"
g: Union[int, str] = 10
g: Union[int, str] = "hello"

def h(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

Union[str, None] == Optional[str]

def i(name: str | None = None):
    pass
def i(name: Optional[str] = None):
    pass
def i(name: Union[str, None] = None):
    pass

def j(name: Optional[str]):
    # name is not optional!
    # j()          --> through an error
    # j(name=None) --> it is Ok
    pass
def j(name: str | None):
    # name is really optional
    pass

# CLASSES AS TYPES

from pydantic import BaseModel
from datetime import datetime
from typing import Annotated

class Person:
    def __init__(self, name: str):
        self.name = name
def get_person_name(one_person: Person):
    print(one_person.name)

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"]
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

def say_hello(name: Annotated[str, "this is just metadata"]):
    pass

