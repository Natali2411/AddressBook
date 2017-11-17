def test_group_create(app, login_admin):
    app.open_group_page()
    app.create_group(name="1234", header="12345", footer="1234")
    # TODO: verification of message
    app.return_to_group_page()
    # TODO: Verification that group added
