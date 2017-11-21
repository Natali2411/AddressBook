import pytest
from selenium import webdriver
from models.addressbook_app import AddressBookApp
from models.addressbook_db import AddressBookDB
from models.group import Group

@pytest.fixture(scope="session")
def app():
    driver = webdriver.Chrome()
    base_url = "http://localhost/addressbook/"
    app = AddressBookApp(driver, base_url)
    yield app
    app.quit()

@pytest.fixture()
def db():
    config = {"host": 'localhost', "user": 'root', "password": '', "db": 'test'}
    db = AddressBookDB(**config)
    yield db
    db.close()

@pytest.fixture()
def login_admin(app):
    app.login(username="admin", password="secret")
    yield
    app.logout()

groups_list = [Group(name="friend1", header="friend1", footer="friend1")]

repr_list = [str(g) for g in groups_list]

@pytest.fixture(params=groups_list, ids=repr_list)
def group (request):
    return request.param