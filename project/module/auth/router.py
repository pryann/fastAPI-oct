from fastapi import APIRouter


auth_router = APIRouter(prefix="/api/auth", tags=["Auth"])


@auth_router.post("/registration", status_code=201)
async def register_user():
    pass


@auth_router.post("/login", status_code=204)
async def login():
    pass


@auth_router.post("/logout", status_code=204)
async def logout():
    pass
