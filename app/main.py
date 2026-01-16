from fastapi import FastAPI

app = FastAPI(title = "Running the backend")
users = [
    {"id": 1, "name": "Alice", "age": 22},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 22},
]

@app.get("/")

def root():
    return {"message":"Hello, I am alive!"}

@app.get("/health")

def heath():
    return {"status": "OK"}

@app.get("/users")

def get_user(age: int | None = None):
    if age is None:
        return users
    
    return [user for user in users if user["age"] == age]

@app.get("/userss/{user_id}")

def userss(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
        return {"status": "user not found 404"}

@app.get("/search")

def search(name: str = "Guest", age: int |None = None ):
    return {
        "name": name,
        "age": age,
        "status": "working"
    }