import string
import random
import secrets

def create_password():
    password = ''

    for i in range(random.randint(6,10)):
        password += secrets.choice(string.ascii_lowercase)

    for i in range(random.randint(2,5)):
        password += secrets.choice(string.ascii_uppercase)

    for i in range(random.randint(2,5)):
        password += secrets.choice(string.digits)

    for i in range(random.randint(2,4)):
        password += secrets.choice(string.punctuation)

    password = [n for n in password]
    secrets.SystemRandom().shuffle(password)
    password = ''.join(password)
    return password





