class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        self.open_edit_contact_page()
        self.fill_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, Contact):
        self.change_field_value("firstname", Contact.firstname)
        self.change_field_value("lastname", Contact.lastname)
        self.change_field_value("mobile", Contact.mobile)
        self.change_field_value("email", Contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_css_selector("[title=Edit]").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("[value=Update]").click()

    def open_edit_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php")