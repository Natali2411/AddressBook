def test_group_create(app, login_admin):
    app.open_group_page()
    app.create_group(name="group2", header="12345", footer="1234")
    # TODO: verification of message
    assert "A new group has been entered into the address book." in app.wd.find_element_by_id("content").text
    app.return_to_group_page()
    # TODO: Verification that group added
    assert "group2" in app.wd.find_element_by_id("content").text

