from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from app.database import get_db_connection
from app.models import User
from fastapi.middleware.cors import CORSMiddleware
from app.ai import get_mock_ai_response

app = FastAPI(title="ai assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for the AI route
class AIRequest(BaseModel):
    question: str

def simple_hash(text: str) -> str: 
    return '-'.join(str(ord(c)) for c in text)

@app.post("/register")
def register(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        exists = cursor.execute("SELECT * FROM accounts WHERE username = ?", (user.username,)).fetchone()
        if exists:
            return {"message": "username already exists"}

        cursor.execute("INSERT INTO accounts(username, password) VALUES (?, ?)", 
                       (user.username, simple_hash(user.password)))
        conn.commit()
        
        row = cursor.execute("SELECT id FROM accounts WHERE username = ?", (user.username,)).fetchone()
        return {"user_id": row["id"], "username": user.username}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.post("/login")
def login(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", 
                            (user.username, simple_hash(user.password))).fetchone()
    conn.close()
    if result:
        return {"user_id": result["id"], "username": result["username"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/history/{username}")
def history(username: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    results = cursor.execute("SELECT role, content FROM messages WHERE username = ? ORDER BY timestamp ASC", 
                             (username,)).fetchall()
    conn.close()
    return [dict(row) for row in results]

@app.post("/ai/ask/{user_id}")
def ask_ai(user_id: int, req: AIRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        user = cursor.execute("SELECT username FROM accounts WHERE id = ?", (user_id,)).fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        cursor.execute("INSERT INTO messages(username, role, content) VALUES (?, ?, ?)", 
                       (user["username"], "user", req.question))
        
        answer = get_mock_ai_response(req.question) 
        
        cursor.execute("INSERT INTO messages(username, role, content) VALUES (?, ?, ?)", 
                       (user["username"], "ai", answer))
        conn.commit()
        return {"answer": answer}
    finally:
        conn.close()

@app.put("/update/{user_id}")
def update(user_id: int, user: User):
    conn = get_db_connection() 
    cursor = conn.cursor()
    # Check if NEW username is taken by SOMEONE ELSE
    exists = cursor.execute("SELECT * FROM accounts WHERE username = ? AND id != ?", (user.username, user_id)).fetchone()

    if not exists:
        cursor.execute("UPDATE accounts SET username = ?, password = ? WHERE id = ?", 
                       (user.username, simple_hash(user.password), user_id))
        conn.commit()
        conn.close()
        return {"user_id": user_id, "username": user.username}
    
    conn.close()   
    return {"message": "username already exists"}