import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_positive(client):
    response = client.post('/predict', json={'text': 'This is good'})
    assert response.status_code == 200
    assert response.get_json()['sentiment'] == 'Positive'

def test_predict_negative(client):
    response = client.post('/predict', json={'text': 'This is bad'})
    assert response.status_code == 200
    assert response.get_json()['sentiment'] == 'Negative'

def test_predict_no_text(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()
