import requests
import pytest

from csv import reader

def http_method(name: str):
    return requests.get if name.lower() == "get" else requests.post

reader = reader(open("../data_files/data_03_json_placeholder.csv", 'r'))
headers = next(reader)

comments = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')

term = requests.request("DELETE", "https://jsonplaceholder.typicode.com/posts/201")

@pytest.mark.parametrize(headers, reader)
def test_json_place_holder(url, method, status):
    assert http_method(method)(url, allow_redirects=False).status_code == int(status)


@pytest.mark.parametrize('post_id', [1, 8, 30, 50],
                         ids=["one_post", "eight_post", "thirty_post", "fifty_post"])
def test_check_post_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


def test_comments_head():\
    assert comments.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_comments_json_not_null():\
    assert comments.json() != ''


def test_delete():
    assert term.status_code == 200