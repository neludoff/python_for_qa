from model.Contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        self.open_add_new_page()
        self.fill_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cash = None

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
        self.delete_contact_by_id(0)

    def delete_contact_by_id(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("[value=Delete]").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def modify_first_contacr(self, new_contact_data):
        self.modify_contact_by_id(0, new_contact_data)


    def modify_contact_by_id(self, index, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("[value=Update]").click()
        self.contact_cash = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("[title=Edit]")[index].click()

    def open_add_new_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("entry"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cash = []
            for element in wd.find_elements_by_css_selector(('[name=entry]')):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                contact_data = element.find_elements_by_css_selector("td")
                lastname = contact_data[1].text
                firstname = contact_data[2].text
                self.contact_cash.append(Contact(firstname=firstname, lastname=lastname, id=id))
                var = self.contact_cash
        return list(self.contact_cash)