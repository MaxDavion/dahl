# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    def open_litecart_admin(self):
        self.wd.get('http://localhost/litecart/admin/')

    def login_as(self, username, password):
        self.wd.find_element(By.NAME, 'username').click()
        self.wd.find_element(By.NAME, 'username').send_keys(username)
        self.wd.find_element(By.NAME, 'password').click()
        self.wd.find_element(By.NAME, 'password').send_keys(password)
        self.wd.find_element(By.NAME, 'login').click()




    @property
    def number_menu_item(self):
        ''' Кол-во пунктов меню
        '''
        return len(self.wd.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app-"))

    @property
    def number_subitem_for_menu_item(self):
        ''' Кол-во пунктов под-меню для каждого пункта меню
        '''
        return len(self.wd.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app- li"))

    def click_side_menu_item(self, item):
        ''' Выбрать пункт меню по его индексу
        '''
        self.wd.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app-")[item].click()

    def click_side_menu_sub_item(self, item):
        ''' Выбрать пункт под-меню по его индексу
        '''
        self.wd.find_elements(By.CSS_SELECTOR, "#box-apps-menu #app- li")[item].click()

    def quit(self):
        self.wd.quit()




