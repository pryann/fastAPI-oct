from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from database import get_session
from models import UserModel
from schemas import User, UserCreate, UserUpdate
from sqlalchemy.orm import Session
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/users", response_model=list[User])
async def get_users(db: Session = Depends(get_session)):
    stmt = select(UserModel)
    users = db.scalars(stmt).all()
    return users


@app.get("/users/{user_id}", response_model=User)
async def find_user_by_id(user_id: int, db: Session = Depends(get_session)):
    stmt = select(UserModel).where(UserModel.id == user_id)
    user = db.scalars(stmt).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_session)):
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.patch("/users/{user_id}", response_model=User)
async def update_user(
    user_id: int, user: UserUpdate, db: Session = Depends(get_session)
):
    stmt = select(UserModel).where(UserModel.id == user_id)
    existing_user = db.scalars(stmt).first()

    if existing_user:
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(existing_user, key, value)
        db.commit()
        db.refresh(existing_user)
        return existing_user

    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", status_code=204)
async def remove_user(user_id: int, db: Session = Depends(get_session)):
    stmt = select(UserModel).where(UserModel.id == user_id)
    existing_user = db.scalars(stmt).first()

    if existing_user:
        db.delete(existing_user)
        db.commit()
        return

    raise HTTPException(status_code=404, detail="User not found")
