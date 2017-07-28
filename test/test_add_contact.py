# -*- coding: utf-8 -*-
from model.Contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen))) + "@" + \
           "".join(random.choice(string.ascii_letters) for i in range(random.randrange(maxlen))) + "." + \
           "".join(random.choice(string.ascii_letters) for i in range(random.randrange(maxlen)))

def random_phone(maxlen):
    return "".join(random.choice(string.digits) for i in range(random.randrange(maxlen)))

testdata = [Contact(firstname="", lastname="", mobilephone="", secondaryphone="", workphone="",
                 homephone="", email="", email2="", email3="")]+\
           [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
                    mobilephone=random_phone(10), homephone=random_phone(10), 
                    workphone=random_phone(10), secondaryphone=random_phone(10),email=random_email("email", 10),
                    email2=random_email("email2",10), email3=random_email("email3", 10),
                    all_address_from_home_page=random_string("address",30))
        for i in range (2)
     ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    # app.contact.count() is a hash function
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)