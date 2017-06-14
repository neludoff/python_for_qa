from model.Contact import Contact

def test_modify_contact(app):
    app.contact.modify_first_contact((Contact(firstname ="Steve", lastname ="Jobs", mobile ="123")))