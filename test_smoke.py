# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.common.by import By
from hamcrest import *


class TestAdminLitecart:

    def test_user_can_open_litecart_admin_page(self, admin_app):
        admin_app.login_as(username='admin', password='admin')

    def test_user_can_clicked_all_side_menu_and_see_page_header(self, admin_app):
        admin_app.login_as(username='admin', password='admin')
        for i in xrange(admin_app.number_menu_item):
            admin_app.click_side_menu_item(i)
            assert_that(admin_app.wd.find_element(By.XPATH, "//h1").text, not_none())
            for y in xrange(admin_app.number_subitem_for_menu_item):
                admin_app.click_side_menu_sub_item(y)
                assert_that(admin_app.wd.find_element(By.XPATH, "//h1").text, not_none())

class TestWebLitecart:

    def test_user_can_see_one_sticker_for_every_product_card(self, web_app):
        for i in web_app.product_card:
            stickers_on_product_card = i.find_elements(By.CSS_SELECTOR, ".sticker")
            assert_that(len(stickers_on_product_card), equal_to(1))
            assert_that(stickers_on_product_card[0].text, not_none())


