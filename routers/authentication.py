from fastapi import APIRouter
from database import database
from service import authentication
from models import UserNameEmail

# database.findUser(email)
router = APIRouter(
    responses={404: {"description": "Not found"}},
)

@router.get("/signin", response_model=UserNameEmail)
async def get_items():
    return {"message": authentication.test()}