from fastapi import FastAPI
from app.models import UserCreate

app = FastAPI(title= "AI assitant app")
users = []

@app.get("/")

def root():
    return {"greeting": "hello to this app"}

@app.get("/users")

def get_users():
    return users

@app.get("/users/{user_id}")

def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"status": "user not found"}

@app.post("/users")

def add_user(user: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "age": user.age
    }

    users.append(new_user)
    return new_user