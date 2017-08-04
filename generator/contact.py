from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:n", ["file","number of contacts"])
except getopt.GetoptError as err:
    # print help information and exit:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if 0 == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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



testdata = [Contact(firstname="", lastname="", mobilephone="", email="")]+ [
        Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
                mobilephone=random_phone(20), secondaryphone=random_phone(20), workphone=random_phone(20),
                homephone=random_phone(20), email=random_email("email", 20), email2=random_email("email2", 20),
                email3=random_email("email3", 20))
        for i in range (n)
     ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))