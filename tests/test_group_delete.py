import random

def test_delete_group(app, login_admin, db):
    index = random.randrange(app.count_groups())
    app.open_group_page()
    c1 = app.count_groups()
    del_id = app.delete_group_by_number(index)
    # TODO: verification of message\
    assert "Group has been removed." in app.wd.find_element_by_id("content").text
    app.return_to_group_page()
    c2 = app.count_groups()
    # TODO: Verification that group removed
    assert c1 != c2

    for i in db.get_groups_id():
        print(i)
    #assert del_id in db.get_groups()["group_id"]