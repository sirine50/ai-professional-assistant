from fastapi import FastAPI

app = FastAPI(title = "Running the backend")

@app.get("/")

def root():
    return {"message":"Hello, I am alive!"}

@app.get("/health")

def heath():
    return {"status": "OK"}

@app.get("/job")

def heath():
    return {"job": "enployed"}