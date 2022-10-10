import requests
import pytest



def test_status_code():
    response = requests.get("https://petstore.swagger.io/v2/pet/1")
    assert response.status_code == 200

def test_namepet():
    response = requests.get("https://petstore.swagger.io/v2/pet/1")
    print(response.json())
    assert response.json()['name'] == 'doggie'
