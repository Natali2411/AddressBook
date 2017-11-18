def test_login(app):
    app.login(username="admin", password="secret")
    assert app.internal_page.is_this_page()
    assert app.internal_page.username_indicator == "admin"
    app.logout()
    assert app.login_page.is_this_page