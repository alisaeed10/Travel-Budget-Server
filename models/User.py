from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'
    email: str
    password: str

class UserNameEmail(BaseModel):
    