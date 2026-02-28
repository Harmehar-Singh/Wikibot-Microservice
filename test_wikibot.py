from fastapi.testclient import TestClient

from wikibot import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Wikibot Microservice!"}


def test_scrape_success():
    # This uses the real wikipedia API; for unit tests you might mock it.
    response = client.post(
        "/scrape",
        json={"name": "Python (programming language)", "length": 1},
    )
    assert response.status_code == 200
    body = response.json()
    assert "summary" in body
    assert isinstance(body["summary"], str)
    assert len(body["summary"]) > 0