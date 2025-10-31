from pydantic import BaseModel, EmailStr


class Registration(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    # need to confirm that the user accepted the terms
    terms_accepted: bool
    newsletter: bool


class Login(BaseModel):
    email: EmailStr
    password: str
