# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class Application:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    def quit(self):
        self.wd.quit()

