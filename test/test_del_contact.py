from model.Contact import Contact

def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", email="test@test.com"))
    app.contact.delete_first_contact()