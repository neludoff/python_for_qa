# -*- coding: utf-8 -*-
import pytest
from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="New group", header="Group header", footer="group footer"))
    app.logout()


