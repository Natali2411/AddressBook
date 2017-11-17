import pytest
from selenium import webdriver
from models.addressbook_app import AddressBookApp


@pytest.fixture(scope="session")
def app():
    driver = webdriver.Chrome()
    base_url = "http://localhost/addressbook/"
    app = AddressBookApp(driver, base_url)
    yield app
    app.quit()

@pytest.fixture()
def login_admin(app):
    app.login(username="admin", password="secret")
    yield
    app.logout()