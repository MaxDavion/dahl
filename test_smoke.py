# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.common.by import By
from hamcrest import *
import time


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

    def test_that_countries_and_zones_on_countries_page_are_sorted_alphabetically(self, admin_app):
        admin_app.login_as(username='admin', password='admin')
        admin_app.open_page("?app=countries")

        countries_list = []
        for row in admin_app.countries_table:
            (number, code, name, zones) = map(lambda x: x.strip(), row.get_attribute("textContent").strip().split(u"\n"))
            countries_list.append((name, zones))
        assert_that(countries_list, equal_to(sorted(countries_list)))

        for i in filter(lambda (name, zones): int(zones) > 0, countries_list):
            admin_app.open_country_page_by_index(countries_list.index(i))
            zones_list = []
            for row in admin_app.zones_table:
                (number, code, name) = map(lambda x: x.strip(), row.get_attribute("textContent").strip().split(u"\n"))
                zones_list.append(name)
            assert_that(zones_list, equal_to(sorted(zones_list)))
            admin_app.wd.back()

    def test_that_zones_on_zones_page_are_sorted_alphabetically(self, admin_app):
        admin_app.login_as(username='admin', password='admin')
        admin_app.open_page("?app=geo_zones")

        for i in xrange(admin_app.number_items):
            admin_app.open_geo_zone_page(i)
            zones_list = [zone.text for zone in admin_app.selected_zones_list]
            assert_that(zones_list, equal_to(sorted(zones_list)))
            admin_app.wd.back()






class TestWebLitecart:

    def test_user_can_see_one_sticker_for_every_product_card(self, web_app):
        for i in web_app.product_card:
            stickers_on_product_card = i.find_elements(By.CSS_SELECTOR, ".sticker")
            assert_that(len(stickers_on_product_card), equal_to(1))
            assert_that(stickers_on_product_card[0].text, not_none())



