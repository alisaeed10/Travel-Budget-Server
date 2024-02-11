from fastapi import APIRouter, Depends, HTTPException
from database import database

# database.findUser(email)
router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_items():
    return "hello world"

# @router.get("/{item_id}")