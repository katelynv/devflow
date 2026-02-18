from fastapi import APIRouter
from app.schemas.project import Project

router = APIRouter()

projects = [
  {"id": 1, "name": "Backend API", "description": "Build FastAPI backend"},
  {"id": 2, "name": "Frontend UI", "description": "Build React frontend"}
]

@router.get("/")
def get_projects():
  return projects

@router.post("/")
def create_project(project: Project):
  new_project = {
    "id": len(projects) + 1,
    "name": project.name,
    "description": project.description
  }
  projects.append(new_project)
  return new_project

