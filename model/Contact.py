class Contact:
    def __init__(self, firstname=None, lastname=None, mobile=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and self.id == other.id