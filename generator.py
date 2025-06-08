import random
import string


def random_name(length):
     a = ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(length)])
     return a
def random_email(domain= 'gmail.com'):
     email_length = random.randint(4, 6)
     a = ''.join([random.choice(string.ascii_lowercase) for i in range(email_length)])
     b = f"{a}@{domain}"
     return b
def random_password():
     password_length = random.randint(4, 7)
     a = ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(password_length)])
     return a
def random_view():
     return random.choice(['dog','cat','reptile', 'hamster', 'parrot'])
def random_age():
     return str(random.randint(0,30))
print(random_age())
def random_gender():
     return random.choice(['Female','Male'])