import requests
import pytest

req = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
array = req.json()
petId = ""
petName = ""

for pet in array:
    if "name" in pet:
        print(pet)
        petId = pet['id']
        petName = pet['name']
        break


def test_status_code():
    response = requests.get("https://petstore.swagger.io/v2/pet/" + str(petId))
    assert response.status_code == 200


def test_name_pet():
    response = requests.get("https://petstore.swagger.io/v2/pet/" + str(petId))
    print(response.json()['name'])
    assert response.json()['name'] == petName
