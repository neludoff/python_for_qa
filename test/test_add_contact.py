# -*- coding: utf-8 -*-
from model.Contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname ="Steve", lastname ="Jobs", mobile ="911", email='mark@ivanov.com'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)