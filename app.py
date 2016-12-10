# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class AdminApp:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    base_url = 'http://localhost/litecart/admin/'

    def open_litecart_admin(self):
        self.wd.get(self.base_url)

    def open_page(self, url):
        self.wd.get(self.base_url + url)

    def login_as(self, username, password):
        self.wd.find_element(By.NAME, 'username').click()
        self.wd.find_element(By.NAME, 'username').send_keys(username)
        self.wd.find_element(By.NAME, 'password').click()
        self.wd.find_element(By.NAME, 'password').send_keys(password)
        self.wd.find_element(By.NAME, 'login').click()

    def quit(self):
        self.wd.quit()

    # --------------------    Side Menu   -----------------------

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

    # --------------------    Countries   -----------------------

    @property
    def countries_table(self):
        ''' Получить список строк таблицы стран
        '''
        return self.wd.find_elements(By.CSS_SELECTOR, '[name="countries_form"] tr.row')

    def open_country_page_by_index(self, index):
        ''' Среди всех стран в таблице выбрать страну по индексу и перейти в нее
        '''
        self.countries_table[index].find_element(By.CSS_SELECTOR, "a").click()

    @property
    def zones_table(self):
        ''' Получить список строк таблицы зон
        '''
        return self.wd.find_elements(By.CSS_SELECTOR, '.dataTable tr:not(.header)')[:-1]


    # --------------------    Geo Zones   -----------------------

    @property
    def number_items(self):
        ''' Кол-во пукнтов геозон в таблице
        '''
        return len(self.wd.find_elements(By.CSS_SELECTOR, "[name='geo_zones_form'] tr.row"))

    def open_geo_zone_page(self, item):
        ''' Перейти на страницу выбранного пункта
        '''
        row = self.wd.find_elements(By.CSS_SELECTOR, "[name='geo_zones_form'] tr.row")[item]
        row.find_element(By.CSS_SELECTOR, "a:not([title])").click()

    @property
    def selected_zones_list(self):
        ''' Возвращает список элементов выбранных зон из таблыицы зон
        '''
        return self.wd.find_elements(By.CSS_SELECTOR, ".dataTable select[name*=zone_code] option[selected]")



class WebApp:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    def open_litecart_web(self):
        self.wd.get('http://localhost/litecart/')

    @property
    def product_card(self):
        ''' Список карточек продукта на странице
        '''
        return self.wd.find_elements(By.CSS_SELECTOR, ".product")

    def quit(self):
        self.wd.quit()



