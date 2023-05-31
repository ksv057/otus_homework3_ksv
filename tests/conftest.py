import json

import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    # parser.addoption("--url", action="store", default="https://jsonplaceholder.typicode.com")
    # parser.addoption("--url", action="store", default="https://dog.ceo")
    parser.addoption("--status_code", action="store", type=int, default=200)

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

@pytest.fixture(scope="module")
def session():
    return requests.Session()