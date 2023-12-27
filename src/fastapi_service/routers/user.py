from db.db_client import DBClient
from fastapi import APIRouter, HTTPException
from db.models import User
from dtos import CreateUserSchema, CreateUserResponse, UpdateUserSchema, GetUserResponse, UpdateUserResponse


router = APIRouter(
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"}
    }
)

db_client = DBClient()


@router.get("/api/v1/users", status_code=200, tags=["User"])
async def get_users():
    users = await db_client.retrieve_all_users(User)
    return users


@router.get("/api/v1/users/{user_id}", response_model=GetUserResponse, status_code=200, tags=["User"])
async def get_user(user_id: str):
    user = await db_client.retrieve_one_user(user_id)
    return user


@router.post("/api/v1/users", response_model=CreateUserResponse, status_code=201, tags=["User"])
async def create_user(payload: CreateUserSchema):
    row_id = await db_client.insert_user(payload)
    return CreateUserResponse(id=row_id)


@router.post("/api/v1/users/{user_id}", response_model=UpdateUserResponse, status_code=200, tags=["User"])
async def update_user(user_id: str, payload: UpdateUserSchema):
    user = await db_client.update_user(user_id, payload)
    return user


@router.delete("/api/v1/users/{user_id}", status_code=204, tags=["User"])
async def delete_user(user_id: str):
    await db_client.delete_user(user_id)
