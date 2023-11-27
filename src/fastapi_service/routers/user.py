from uuid import UUID

from fastapi import APIRouter, HTTPException

from db.user_db import UpdateUser, User, user_db

router = APIRouter(
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/api/v1/users")
async def get_users():
    return user_db


@router.get("/api/v1/users/{id}")
async def get_user(user_id: UUID):
    for user in user_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {user_id}")


@router.post("/api/v1/users")
async def create_user(user: User):
    user_db.append(user)
    return {"id": user.id}


@router.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, user_id: UUID):
    for user in user_db:
        if user.id == user_id:
            if user_update.name is not None:
                user.name = user_update.name
            if user_update.role is not None:
                user.role = user_update.role
            return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {user_id}")


@router.delete("/api/v1/users/{id}")
async def delete_user(user_id: UUID):
    for user in user_db:
        if user.id == user_id:
            user_db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f"Delete user failed, id {user_id} not found.")
