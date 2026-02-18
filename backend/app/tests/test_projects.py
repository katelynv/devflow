from fastapi.testclient import TestClient 
from app.main import app

client = TestClient(app)

def test_create_project_success():
  response = client.post(
    "/projects",
    json={"name": "test project", "description": "Testing create"}
  )
  assert response.status_code == 200
  data = response.json() 
  assert data["name"] == "test project"
  assert data["description"] == "Testing create"
  assert "id" in data

def test_create_project_invalid_type():
  response = client.post(
    "/projects",
    json={"name": 123, "description": "invalid type"}
  )
  assert response.status_code == 422
  data = response.json()
  assert "detail" in data
