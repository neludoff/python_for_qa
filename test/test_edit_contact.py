from model.Contact import Contact

def test_change_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact((Contact(firstname ="Steve", lastname ="Jobs", mobile ="123", email='steve@apple.com')))
    app.session.logout()