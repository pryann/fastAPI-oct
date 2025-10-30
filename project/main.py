from fastapi import FastAPI
from database import Base, engine
from module.user.router import user_router
from module.user.exception_handler import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI()

register_exception_handlers(app)
app.include_router(user_router)
