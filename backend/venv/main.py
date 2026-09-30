from fastapi import FastAPI 

app = FastAPI()

@app.get("/")

def home():
    return {"message": "app backend is running :3"}