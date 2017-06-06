class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        self.open_contact_page()

        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php")