import json
from fastapi.testclient import TestClient
from main import app
from generate_users import generate_user
from SQL_ORM_API import save_users_data

def test_response_question():
    client = TestClient(app)

    # Generate user data
    integer = 5
    data = generate_user(integer)

    # Mock the save_users_data function
    def mock_save_users_data(data_dict):
        assert data_dict == data
        return

    # Replace the original save_users_data function with the mock function
    save_users_data_orig = save_users_data
    save_users_data = mock_save_users_data

    # Make a POST request to the endpoint
    response = client.post(f"/api/{integer}")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response body matches the generated user data
    assert response.json() == data

    # Restore the original save_users_data function
    save_users_data = save_users_data_orig