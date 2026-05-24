from  Flask_app_project.src.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Enterprise Flask CI/CD Architecture" in response.data