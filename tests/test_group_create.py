import pytest
from models.group import Group

def test_group_create(app, login_admin, group, db):
    old_list = db.get_groups()
    app.open_group_page()
    app.create_group(group)
    # TODO: verification of message
    assert "A new group has been entered into the address book." in app.wd.find_element_by_id("content").text
    app.return_to_group_page()
    # TODO: Verification that group added
#    assert "group2" in app.wd.find_element_by_id("content").text
    new_list = db.get_groups()
    assert len(new_list) == len(old_list) + 1
    assert group == new_list[-1]

