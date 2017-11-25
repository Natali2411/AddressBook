import pytest
from selenium import webdriver
from models.addressbook_app import AddressBookApp
from models.addressbook_db import AddressBookDB
from models.group import Group
import os
import json

@pytest.fixture(scope="session")
def config():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(filename)as f:
        return json.load(f)

@pytest.fixture()
def app(config,selenium):
    driver = selenium #webdriver.Chrome()
    base_url = config["web"]["base_url"]
    app = AddressBookApp(driver, base_url)
    yield app
    app.quit()

@pytest.fixture()
def db(config):
    #config = {"host": 'localhost', "user": 'root', "password": '', "db": 'test'}
    db = AddressBookDB(**config["db"])
    yield db
    db.close()

@pytest.fixture()
def login_admin(app, config):
    app.login(config["web"]["user"], password=config["web"]["password"])
    yield
    app.logout()

groups_list = [Group(name="friend1", header="friend1", footer="friend1"),
               Group(name="friend2", header="friend2", footer="friend2")]

repr_list = [str(g) for g in groups_list]

@pytest.fixture(params=groups_list, ids=repr_list)
def group (request):
    return request.param
'''
#check
@pytest.fixture()
def fillDB(app, db):
    db.import_groups()
    yield True
    db.clean_groups()
'''