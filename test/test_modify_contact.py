from model.Contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", email="test@test.com"))
    app.contact.modify_first_contact((Contact(firstname ="Steve", lastname ="Jobs", mobile ="123")))