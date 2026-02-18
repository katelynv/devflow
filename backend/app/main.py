from fastapi import FastAPI 
from app.routes import projects

app = FastAPI()

@app.get('/')
def root():
  return {"message": "DevFlow API is running"}


@app.get("/health")
def health_check():
  return {"status": "ok"}

app.include_router(projects.router, prefix='/projects')