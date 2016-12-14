#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from faker import Factory
import random
import string


class User:

    def __init__(self, firstname=None, lastname=None, address1=None,  postcode=None, city=None, country=None,
                 email=None, phone=None, password=None, confirmed_password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.postcode = postcode
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone
        self.password = password
        self.confirmed_password = confirmed_password

    def __repr__(self):
            return 'firstname:%s lastname:%s email:%s' % (self.firstname, self.lastname, self.email)




# --------------------    Data Generator   -----------------------


fake = Factory.create()

def generate_random_data_for_user(**kwargs):
    password = fake.password()
    user = User(firstname=kwargs['firstname'] if 'firstname' in kwargs else fake.name().split(" ", 1)[0],
                lastname=kwargs['lastname'] if 'lastname' in kwargs else fake.name().split(" ", 1)[1],
                address1=kwargs['address1'] if 'address1' in kwargs else fake.street_address(),
                postcode=kwargs['postcode'] if 'postcode' in kwargs else '114443',
                city=kwargs['city'] if 'city' in kwargs else fake.city(),
                country=kwargs['country'] if 'country' in kwargs else generate_random_country(),
                phone=kwargs['phone'] if 'phone' in kwargs else '79000000000',
                email=kwargs['email'] if 'email' in kwargs else generate_random_email(),
                password=kwargs['password'] if 'password' in kwargs else password,
                confirmed_password=kwargs['confirmed_password'] if 'confirmed_password' in kwargs else password)
    return user


def generate_random_email():
    symbols = string.digits + string.ascii_letters.lower()
    random_string = "".join([random.choice(symbols) for i in range(random.randrange(5, 7))]).rstrip()
    return clear_string(random_string) + '@mailinator.com'


def generate_random_country():
    countries_list = [ u'Albania', u'Russian Federation', u'Anguilla']
    return random.choice(countries_list)


def clear_string(str):
    return re.sub(r'\s+', ' ', str)








