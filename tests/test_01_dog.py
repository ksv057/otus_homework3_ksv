import pytest
import requests

from csv import reader

def http_method(name: str):
    return requests.get if name.lower() == "get" else requests.post

reader = reader(open("../data_files/data_01_dog.csv", 'r'))
headers = next(reader)

@pytest.mark.parametrize(headers, reader)
def test_reader_dog(url, method, status):
    assert http_method(method)(url, allow_redirects=False).status_code == int(status)

@pytest.mark.parametrize('count', [1, 5, 50], ids=['one_image', 'five_images', 'fifty_images'])
def test_count_images(count):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{count}")
    assert response.status_code == 200
    assert response.json() != ''
    assert len(response.json()["message"]) == count
    assert response.json()["status"] == "success"

random = requests.get('https://dog.ceo/api/breeds/image/random')

def test_random_status_code():\
    assert random.status_code == 200 & \
           random.status_code != 404 & \
           random.status_code != 500

images = requests.get('https://dog.ceo/api/breed/hound/images')
def test_images_head():\
    assert images.headers['Content-Type'] == 'application/json'

def test_images_json_not_null():\
    assert images.json() != ''



















# reader = reader(open("test_data_dog_negative.csv", 'r'))
# headers = next(reader)
#
# @pytest.mark.parametrize(headers, reader)
# def test_reader_neg(url, method, status):
#     assert http_method(method)(url, allow_redirects=False).status_code == int(status)
