from typing import Annotated
from fastapi import FastAPI, Form
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/registration")
async def registration(
    user_name: Annotated[str, Form()],
    email_address: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    # hash pwd, save to DB
    user = {
        "user_name": user_name,
        "email_address": email_address,
        "password": password,
    }
    print("Registered user:", user)

    return {
        "user_name": user_name,
        "email_address": email_address,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
