
def test_modify_group(app, login_admin):
    ch = app.wd.find_elements_by_name("selected[]")
    if ch:
        ch[0].click()
        app.wd.find_element_by_xpath("//div[@id='content']//input[@name='edit']").click()
        app.wd.find_element_by_name("group_name").send_keys("new_group_name")
        app.wd.find_element_by_name("group_header").send_keys("new_header_name")
        app.wd.find_element_by_name("group_footer").send_keys("new_footer_name")
