# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.Contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create(Contact(firstname ="Steve", lastname ="Jobs", mobile ="911", email='mark@ivanov.com'))
    app.session.logout()