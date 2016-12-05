# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.common.by import By
import time
from hamcrest import *

def test_user_can_open_traning_page(litecart):
    litecart.login_as(username='admin', password='admin')

def test_menu_login(litecart):
    litecart.login_as(username='admin', password='admin')
    for i in xrange(litecart.number_menu_item):
        litecart.click_side_menu_item(i)
        assert_that(litecart.wd.find_element(By.XPATH, "//h1").text, not_none())
        for y in xrange(litecart.number_subitem_for_menu_item):
            litecart.click_side_menu_sub_item(y)
            assert_that(litecart.wd.find_element(By.XPATH, "//h1").text, not_none())



