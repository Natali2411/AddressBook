from selenium import webdriver
from models.addressbook_app import AddressBookApp
driver = webdriver.Chrome()
wd = AddressBookApp(driver, "http://localhost/addressbook/")
wd.login('admin', 'secret')
wd.open_group_page()
t = driver.find_elements_by_name("selected[]")
print(t[1].text)
print(t[1].tag_name)
print(t[1].id)
print(t[2].get_attribute("value"))
wd.quit()