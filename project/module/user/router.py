from fastapi import APIRouter, Depends

from .dependency import get_user_service
from .service import UserService
from .schema import User, UserUpdate


user_router = APIRouter(prefix="/api/users", tags=["User"])


@user_router.get("/", response_model=list[User])
async def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_users()


@user_router.get("/{user_id}", response_model=User)
async def find_user(
    user_id: int, user_service: UserService = Depends(get_user_service)
):
    return user_service.find_user(user_id)


@user_router.patch("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_payload: UserUpdate,
    user_service: UserService = Depends(get_user_service),
):
    return user_service.update_user(user_id, user_payload)


@user_router.delete("/{user_id}", status_code=204)
async def remove_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
):
    return user_service.remove_user(user_id)
