from pytest_bdd import given, when, then
from models.group import Group


@given("a group list on app")
def old_group_list(db):
    return db.get_groups()

@given("a new group with <name>, <header>, <footer>")
def group(name, header, footer):
    return Group(name, header, footer)

@when("I add this group")
def create_group(app, login_admin, group):
    app.open_group_page()
    app.create_group(group)
    app.return_to_group_page()

@then("a new group list is equal to old group list with this new group")
def verify_group_created(db, old_group_list, group):
    new_list = db.get_groups()
    assert len(new_list) == len(old_group_list) + 1
    assert group == new_list[-1]