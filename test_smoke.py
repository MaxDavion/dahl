# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.common.by import By


def test_user_can_open_traning_page(app):
    app.wd.get('http://localhost/litecart/admin/')
    app.wd.find_element(By.NAME, 'username').click()
    app.wd.find_element(By.NAME, 'username').send_keys('admin')
    app.wd.find_element(By.NAME, 'password').click()
    app.wd.find_element(By.NAME, 'password').send_keys('admin')
    app.wd.find_element(By.NAME, 'login').click()

