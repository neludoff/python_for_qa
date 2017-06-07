def test_change_groupp(app):
    app.session.login(username="admin", password="secret")
    app.group.change_group()
    app.session.logout()