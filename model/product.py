#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from faker import Factory
import random
import string
from conftest import *


class Product:

    def __init__(self, enabled=None, name=None, code=None,  product_groups=None, quantity=None, image=None,
                 date_valid_from=None, date_valid_to=None, manufacturer_id=None, short_description=None,
                 full_description=None, head_title=None, purchase_price=None, currency_code=None,
                 prices_usd=None, prices_eur=None,):
        self.enabled = enabled
        self.name = name
        self.code = code
        self.product_groups = product_groups
        self.quantity = quantity
        self.image = image
        self.date_valid_from = date_valid_from
        self.date_valid_to = date_valid_to
        self.manufacturer_id = manufacturer_id
        self.short_description = short_description
        self.full_description = full_description
        self.head_title = head_title
        self.purchase_price = purchase_price
        self.currency_code = currency_code
        self.prices_usd = prices_usd
        self.prices_eur = prices_eur

    def __repr__(self):
            return 'name:%s' % (self.name)




# --------------------    Data Generator   -----------------------


fake = Factory.create()

def generate_random_data_for_product(**kwargs):
    product = Product(enabled=kwargs['enabled'] if 'enabled' in kwargs else True,
                name=kwargs['name'] if 'name' in kwargs else __generate_random_product_name(),
                code=kwargs['code'] if 'code' in kwargs else fake.random_int(min=10000, max=99999),
                quantity=kwargs['quantity'] if 'quantity' in kwargs else fake.random_int(min=10, max=999),
                image=kwargs['image'] if 'image' in kwargs else __generate_random_image(),
                date_valid_from=kwargs['date_valid_from'] if 'date_valid_from' in kwargs else fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None),
                date_valid_to=kwargs['date_valid_to'] if 'date_valid_to' in kwargs else fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=None),
                manufacturer_id=kwargs['manufacturer_id'] if 'manufacturer_id' in kwargs else 'ACME Corp.',
                short_description=kwargs['short_description'] if 'short_description' in kwargs else fake.sentence(nb_words=6, variable_nb_words=True),
                full_description=kwargs['full_description'] if 'full_description' in kwargs else fake.text(),
                head_title=kwargs['head_title'] if 'head_title' in kwargs else __generate_random_product_name(),
                purchase_price=kwargs['purchase_price'] if 'purchase_price' in kwargs else fake.random_int(min=100, max=999),
                currency_code=kwargs['currency_code'] if 'currency_code' in kwargs else random.choice(['USD', 'EUR']),
                prices_usd=kwargs['prices_usd'] if 'prices_usd' in kwargs else fake.random_int(min=100, max=999),
                prices_eur=kwargs['prices_eur'] if 'prices_eur' in kwargs else fake.random_int(min=100, max=999))
    return product


def __generate_random_product_name():
    symbols = string.digits + string.ascii_letters
    random_string = "".join([random.choice(symbols) for i in range(random.randrange(5, 7))]).rstrip()
    return 'Auto_Product_' + __clear_string(random_string)


def __generate_random_image():
    images_list = [ 'resousce/test_product_1.JPG',
                    'resousce/test_product_2.JPG']
    return os.path.join(path(), random.choice(images_list))


def __clear_string(str):
    return re.sub(r'\s+', ' ', str)








