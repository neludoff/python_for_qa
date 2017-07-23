import re

def test_contact(app):
    contact_from_home_page = app.contact.get_contact_list_with_all_information()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phone_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_address_from_home_page == contact_from_edit_page.all_address_from_home_page
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                                                        contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))