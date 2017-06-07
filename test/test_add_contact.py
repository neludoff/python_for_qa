# -*- coding: utf-8 -*-
from model.Contact import Contact


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact(firstname ="Steve", lastname ="Jobs", mobile ="911", email='mark@ivanov.com'))
    app.session.logout()