import pytest
import requests
import json

from csv import reader
from jsonschema import validate
from data_files import JSON_SCHEMA_RANDOM
from data_files import JSON_SCHEMA_IMAGES
from data_files import CSV_DATA_01

def http_method(name: str):
    return requests.get if name.lower() == "get" else requests.post

reader = reader(open(CSV_DATA_01, 'r'))
headers = next(reader)

# Проверка набора методов, вычитываем data_01_dog.csv
@pytest.mark.parametrize(headers, reader)
def test_reader_dog(url, method, status):
    assert http_method(method)(url, allow_redirects=False).status_code == int(status)

# Проверяем ответы 1,5, 50 сообщений
@pytest.mark.parametrize('count', [1, 5, 50], ids=['one_image', 'five_images', 'fifty_images'])
def test_count_images(count):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{count}")
    assert response.status_code == 200
    assert response.json() != ''
    assert len(response.json()["message"]) == count
    assert response.json()["status"] == "success"

random = requests.get('https://dog.ceo/api/breeds/image/random')


def test_random_status_code_200():
    assert random.status_code == 200

def test_random_status_code_not_404():
    assert random.status_code != 404

def test_random_status_code_not_500():
    assert random.status_code != 500


# Проверяем json схему random, images
def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        import json
        schema_11 = json.load(f)
    return validate(instance=data, schema=schema_11)

def test_get_random_schema_json():
    resp = requests.get('https://dog.ceo/api/breeds/image/random')
    assert_valid_schema(resp.json(), JSON_SCHEMA_RANDOM)

def test_get_images_schema_json():
    resp = requests.get('https://dog.ceo/api/breed/hound/images')
    assert_valid_schema(resp.json(), JSON_SCHEMA_IMAGES)

# Проверяю значение заголовка
images = requests.get('https://dog.ceo/api/breed/hound/images')
def test_images_head():\
    assert images.headers['Content-Type'] == 'application/json'

# Проверяю, что json НЕ пусой
def test_images_json_not_null():\
    assert images.json() != ''
