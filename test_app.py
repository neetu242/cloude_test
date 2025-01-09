import pytest
from app import app 


def test_hello(client):
    """Test the / route for the 'Hello, World!' response."""
    response = client.get('/')
    assert response.status_code == 200  
    assert response.data == b'Hello, World!' 