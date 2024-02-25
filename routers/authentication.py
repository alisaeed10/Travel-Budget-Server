from fastapi import APIRouter
from service import authentication
import urllib.parse

#from service import authentication
from models import User

# database.findUser(email)
router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@router.get("/login")
# will need user email from the params url
async def get_items(email: str, password: str):
    print("router",email,password)
    user = authentication.get_user(email, password)
    return {"message": "User retrieved successfully!!!", "user": user}
# creating a user
@router.post("/create")
async def create_user(user: User.User):
    print("router",user)
    authentication.create_user(user)
    return {"message": "User created successfully!!!"}