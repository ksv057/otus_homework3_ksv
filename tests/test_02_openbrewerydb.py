import requests
import pytest

from csv import reader

def http_method(name: str):
    return requests.get if name.lower() == "get" else requests.post

reader = reader(open("../data_files/data_02_pivo.csv", 'r'))
headers = next(reader)

@pytest.mark.parametrize(headers, reader)
def test_reader_v2(url, method, status):
    assert http_method(method)(url, allow_redirects=False).status_code == int(status)


@pytest.mark.parametrize("count", [1, 50, 90],
                         ids=['one_breweries_list', 'fifty_breweries_list', 'ninety_breweries_list'])
def test_count_number_of_breweries(count):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?per_page={count}")
    assert response.json()
    assert response.status_code == 200
    assert len(response.json()) == count


param_1 = {'by_type': 'micro'}
micro = requests.get('https://api.openbrewerydb.org/v1/breweries/meta', params=param_1)
def test_status_code():
    assert micro.status_code == 200

def test_head():\
    assert micro.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_json_not_null():\
    assert micro.json() != ''


param_2 = {'page': '15', 'per_page': '3'}
breweries = requests.get('https://api.openbrewerydb.org/v1/breweries', params=param_2)

def test_status_code():
    assert breweries.status_code == 200

def test_head():\
    assert breweries.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_json_not_null():\
    assert breweries.json() != ''