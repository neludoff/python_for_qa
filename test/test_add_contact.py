# -*- coding: utf-8 -*-
from model.Contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname ="Steve", lastname ="Jobs", mobile ="911", email='mark@ivanov.com')
    app.contact.create(contact)
    # app.contact.count() is a hash function
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)