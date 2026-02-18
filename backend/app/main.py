from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
def root():
  return {"message": "DevFlow API is running"}

