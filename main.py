from fastapi import FastAPI

app = FastAPI()




@app.get('/')
def home():
    return {"key":"Hello"}

# uvicorn main:app --reload --port 8080