import random
import string

def email_gen():
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    domain_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    domain_ext = ''.join(random.choices(string.ascii_lowercase, k=5))
    email = user + '@' + domain_name + '.' + domain_ext
    return email

def password_gen():
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
    return password

def name_gen():
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    return name
