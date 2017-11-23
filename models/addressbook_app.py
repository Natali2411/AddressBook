from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.internal_page import InternalPage

class AddressBookApp:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(5)
        self.wd.get(base_url)
        self.wait = WebDriverWait(driver, 5)
        self.wd.maximize_window()
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)

    def login(self, username, password):
        wd = self.wd
        self.login_page.username_field.clear()
        self.login_page.username_field.send_keys(username)
        self.login_page.password_field.clear()
        self.login_page.password_field.send_keys(password)
        self.login_page.submit_button.click()

    def logout(self):
        self.internal_page.logout_button.click()

    def open_group_page(self):
        # Open group page
        self.wd.find_element_by_xpath("//div/div[3]/ul/li[3]/a").click()

    def create_group(self, group):
        wd = self.wd
        # Initialize group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        button = self.wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
        button.click()

    def return_to_group_page(self):
        # Return to group page
        self.wd.find_element_by_link_text("group page").click()

    def delete_group_by_number(self, number):
        checkboxes = self.wd.find_elements_by_name("selected[]")
        id = checkboxes[number].get_attribute("value")
        checkboxes[number].click()
        self.wd.find_element_by_name("delete").click()
        return id

    def count_groups(self):
        self.open_group_page()
        return len(self.wd.find_elements_by_name("selected[]"))

    def quit(self):
        self.wd.quit()
