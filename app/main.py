from fastapi import FastAPI, HTTPException, status
from app.models import UserCreate

app = FastAPI(title= "AI assitant app")
users = []
user_counter = 1


@app.get("/")

def root():
    return {"status": "API running"}

@app.get("/users")

def get_users():
    return users

@app.get("/users/{user_id}")

def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code = 404, detail="User not found")

@app.post("/users", status_code=status.HTTP_201_CREATED)

def add_user(user: UserCreate):
    global user_counter
    
    new_user = {
        "id": user_counter,
        "name": user.name,
        "age": user.age
    }

    users.append(new_user)
    user_counter += 1
    return new_user

@app.put("/users/{user_id}")

def update(user_id: int, user: UserCreate):
    for Existing_user in users:
        if Existing_user["id"] == user_id:
            Existing_user["name"] = user.name
            Existing_user["age"] = user.age
            return Existing_user
    raise HTTPException(status_code = 404, detail="User not found")

@app.delete("/users/{user_id}")

def delete_user(user_id: int):
    for i ,user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return {"status": "user deleted succesfully"}
    raise HTTPException(status_code = 404, detail="User not found")