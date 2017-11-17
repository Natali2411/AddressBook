import random


def test_delete_group(app, login_admin):
    index = random.randrange(app.count_groups())
    app.open_group_page()
    app.delete_group_by_number(index)
    # TODO: verification of message
    app.return_to_group_page()
    # TODO: Verification that group added
