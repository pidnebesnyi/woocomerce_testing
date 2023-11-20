import logging as logger
import random
import string

def generate_random_email_password(domain=None, email_prefix=None):
    logger.debug("Generation Random Email And Password")
    if not domain:
        domain = 'supersqa.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + random_string + '@' + domain

    password_length = 20
    password = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password}

    logger.debug(f'Genetated email and password: {random_info}')

    return random_info

def genarate_random_string(length=10, prefix=None, suffix=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string += prefix

    if suffix:
        random_string += suffix

    return random_string

def genarate_random_number():
    random_number = random.randint(1,1000)
    return random_number
