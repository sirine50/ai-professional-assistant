from fastapi import FastAPI

app = FastAPI(title = "I Professional Assistant")

@app.get("/")

def root():
    return {"status": "backend is running"}