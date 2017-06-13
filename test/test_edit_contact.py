from model.Contact import Contact

def test_change_contact(app):
    app.contact.edit_contact((Contact(firstname ="Steve", lastname ="Jobs", mobile ="123", email='steve@apple.com')))