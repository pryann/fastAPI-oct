from datetime import datetime
from typing import Annotated
from fastapi import Cookie, FastAPI, HTTPException, Header, Response
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Login(BaseModel):
    username: str
    password: str


# DB user
# NEVER store passwords in plain text in real applications
user = {"username": "root", "password": "secret"}


@app.get("/")
async def root(accept_language: Annotated[str | None, Header()] = None):
    lang = accept_language.split(";")[0]
    print(lang)
    if "en" in lang:
        return {"message": "Hello World"}
    elif "hu" in lang:
        return {"message": "Helló Világ"}
    # default
    else:
        return {"message": "Hola Mundo"}


# cookie : saját gépen tárolódik
# szöveges adat
# méret: max 4K
# régen: max 20 db / domain, böngésző függő
# lehet httpOnly: ha ez True akkor JS-ből nem elérhető
# secure: csak https-en küldi el a böngésző
# sameSime: szabályozza, hogy cross-site kéréseknél elküldje-e a böngésző
# expires / max-age: lejárati idő

# szerver létrehozza a token
# elküldui a tokent tartalmazó sütit a kliensnek
# a kliens a sütit elmenti
# JS kiszedi a sütiből a tokent, beleteszi auth headerbe
# szerver ellenőrzi az auth hedert, ksizedi stb


@app.post("/login")
async def login(response: Response, login: Login):
    if login.username == user["username"] and login.password == user["password"]:
        # access accepted
        # generate access (and refresh...) token - JWT
        # user JWT library in real applications
        response.set_cookie(
            key="session_token",
            value=f"user_{user['username']}_{datetime.now().timestamp()}",
            httponly=True,
            secure=True,
            max_age=3600,  # 1h
        )
        return {"message": "Logged in"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/protected-route")
async def protected_route(session_token: str | None = Cookie(None)):
    # need to check expiration etc in real applications
    if session_token:
        return {"message": "You can view this protected content"}
    raise HTTPException(status_code=401, detail="Not authenticated")


@app.get("/logout")
async def logout(response: Response):
    response.set_cookie(key="session_token", value="", max_age=0)
    return {"message": "Logged out"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
