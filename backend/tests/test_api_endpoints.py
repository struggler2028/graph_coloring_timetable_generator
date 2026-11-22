import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.sample_data import get_default_sample_data

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data

def test_sample_data_endpoint():
    response = client.get("/api/sample-data")
    assert response.status_code == 200
    data = response.json()
    assert "courses" in data
    assert "exams" in data
    assert "rooms" in data
    assert "students" in data
    assert len(data["courses"]) > 0
    assert len(data["exams"]) > 0

def test_generate_timetable_endpoint():
    sample_data = get_default_sample_data()
    payload = {
        "students": [s.model_dump() for s in sample_data["students"]],
        "courses": [c.model_dump() for c in sample_data["courses"]],
        "exams": [e.model_dump() for e in sample_data["exams"]],
        "rooms": [r.model_dump() for r in sample_data["rooms"]],
        "algorithm": "dsatur",
        "start_date": "2026-12-01",
        "slots_per_day": 2
    }

    response = client.post("/api/timetable/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["total_slots"] > 0
    assert "conflict_graph" in data
    assert "schedule" in data
    assert len(data["schedule"]) == data["total_slots"]

def test_compare_algorithms_endpoint():
    sample_data = get_default_sample_data()
    payload = {
        "students": [s.model_dump() for s in sample_data["students"]],
        "courses": [c.model_dump() for c in sample_data["courses"]],
        "exams": [e.model_dump() for e in sample_data["exams"]],
        "rooms": [r.model_dump() for r in sample_data["rooms"]],
        "algorithm": "both"
    }

    response = client.post("/api/timetable/compare", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "greedy_metrics" in data
    assert "dsatur_metrics" in data
    assert data["greedy_metrics"]["is_valid_coloring"] is True
    assert data["dsatur_metrics"]["is_valid_coloring"] is True
