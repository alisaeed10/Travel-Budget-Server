# used to format the payload of request and response

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str

class UserNameEmail(BaseModel):
    id:int
    name: str
    email: str