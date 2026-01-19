from fastapi import FastAPI, HTTPException, status
from app.models import UserCreate
from sqlalchemy import  text
from app.database import engine



app = FastAPI(title= "AI assitant app")



with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """))
    conn.commit()



@app.get("/")

def root():
    return {"status": "API running"}

@app.get("/users")

def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        users_list = []
        for row in result:
            users_list.append({
                "id": row[0],
                "name": row[1],
                "age": row[2]
            })
    
    return users_list

@app.post("/users", status_code=status.HTTP_201_CREATED)

def add_user(user: UserCreate):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO users(name, age) VALUES(:name, :age)"),
            {"name": user.name, "age":user.age}
        )
        conn.commit()
        return {"message": "User added"}
    
    
@app.get("/users/{user_id}")

def get_user(user_id: int):
    with engine.connect() as conn:
        results = conn.execute(text("SELECT * FROM users"))
        for row in results:
            if row[0] == user_id:
                return {"id": row[0], "name": row[1], "age": row[2]} 
    
    raise HTTPException(status_code = 404, detail= "User not found")

@app.put("/users/{user_id}")

def update_user(user_id: int , user: UserCreate):
    with engine.connect() as conn:
        conn.execute(text(""" 
            UPDATE users
            SET name = :name,
                age = :age
            where id = :user_id
        """),
        {"name": user.name, "age": user.age, "user_id": user_id}
        )
        conn.commit()
        return {"message": "User updated succefully"}

@app.delete("/users/{user_id}")

def delete_user(user_id: int):
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM users WHERE id = :user_id"), {"user_id": user_id})
        conn.commit()
        return {"message": "User deleted succefully"}