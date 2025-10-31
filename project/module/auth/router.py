from fastapi import APIRouter, Depends, Response
from .schema import Login, Registration
from .dependency import get_auth_service
from .service import AuthService
from ...middleware import get_current_user_id


auth_router = APIRouter(prefix="/api/auth", tags=["Auth"])


@auth_router.post("/registration", status_code=201)
async def registration(
    registration_payload: Registration,
    auth_service: AuthService = Depends(get_auth_service),
):
    return auth_service.registration(registration_payload)


@auth_router.post("/login", status_code=204)
async def login(
    response: Response,
    login_payload: Login,
    auth_service: AuthService = Depends(get_auth_service),
):
    token = auth_service.login(login_payload)
    response.set_cookie(key="access_token", value=token, httponly=True)


@auth_router.post("/logout", status_code=204)
async def logout(
    response: Response,
):
    response.delete_cookie(key="access_token")


@auth_router.get("/me")
async def get_current_user(
    current_user_id: int = Depends(get_current_user_id),
    auth_service: AuthService = Depends(get_auth_service),
):
    return auth_service.me(current_user_id)
