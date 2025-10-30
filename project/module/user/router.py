from fastapi import APIRouter, Depends

from .dependency import get_user_service
from .service import UserService
from .schema import User


router = APIRouter(prefix="/api/users", tags=["User"])


@router.get("/", response_model=list[User])
async def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_users()


@router.get("/{user_id}", response_model=User)
async def find_user():
    pass


@router.patch("/{user_id}", response_model=User)
async def update_user():
    pass


@router.delete("/{user_id}", status_code=204)
async def remove_user():
    pass
