# -*- coding: utf-8 -*-
from hamcrest import *
from selenium.webdriver.common.by import By
from model.user import *
from model.product import *
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

    def test_that_user_can_add_new_product(self, admin_app):
        # Предусловия
        product = generate_random_data_for_product()
        admin_app.login_as(username='admin', password='admin')
        admin_app.open_page("?app=catalog")
        count_products_before = len(admin_app.list_products_in_root_category)
        # Шаги
        admin_app.click_add_new_product()
        admin_app.fill_add_product_form_section_general(enabled=product.enabled, name=product.name, code=product.code,
                                                       quantity=product.quantity, image=product.image,
                                                       date_valid_from=product.date_valid_from,
                                                       date_valid_to=product.date_valid_to)
        admin_app.fill_add_product_form_section_information(manufacturer_id=product.manufacturer_id,
                                                            short_description=product.short_description,
                                                            full_description=product.full_description,
                                                            head_title=product.head_title)
        admin_app.fill_add_product_form_section_prices(purchase_price=product.purchase_price,
                                                       currency_code=product.currency_code,
                                                       prices_usd=product.prices_usd, prices_eur=product.prices_eur)
        admin_app.click_save_product()
        # Проверки
        assert_that(count_products_before + 1, equal_to(len(admin_app.list_products_in_root_category)))
        assert_that([i.text for i in admin_app.list_products_in_root_category], has_item(product.name))

    def test_that_link_open_in_new_tab(self, admin_app):
        admin_app.login_as(username='admin', password='admin')
        admin_app.open_page("?app=countries")
        admin_app.open_country_page_by_index(0)
        main_window = admin_app.wd.current_window_handle
        for i in admin_app.external_links_on_page:
            i.click()
            admin_app.switch_to_new_tab()
            admin_app.wd.close()
            admin_app.wd.switch_to_window(main_window)

    def test_that_browser_log_not_have_messages(self, admin_app):
        admin_app.login_as(username='admin', password='admin')
        admin_app.open_page("?app=catalog&doc=catalog&category_id=1")
        for i in xrange(len(admin_app.list_all_products_in_catalog)):
            admin_app.open_product_page_by_index(i)
            log_text = "\n".join([str(l) for l in admin_app.wd.get_log("browser")])
            assert_that(log_text, empty())
            admin_app.wd.back()



class TestWebLitecart:

    def test_user_can_see_one_sticker_for_every_product_card(self, web_app):
        for i in web_app.product_card:
            stickers_on_product_card = i.find_elements(By.CSS_SELECTOR, ".sticker")
            assert_that(len(stickers_on_product_card), equal_to(1))
            assert_that(stickers_on_product_card[0].text, not_none())

    def test_that_open_right_product_page_when_user_click_on_the_product_in_campaign_section(self, web_app):
        products = web_app.list_product_cards_in_campaign_section
        product_link = products[0].find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        product_name = products[0].find_element(By.CSS_SELECTOR, ".name").text
        product_regular_price = products[0].find_element(By.CSS_SELECTOR, ".regular-price").text
        product_campaign_price = products[0].find_element(By.CSS_SELECTOR, ".campaign-price").text
        products[0].click()
        assert_that(product_link, equal_to(web_app.current_url))
        assert_that(product_name, equal_to(web_app.wd.find_element(By.CSS_SELECTOR, "#box-product h1").text))
        assert_that(product_regular_price, equal_to(web_app.wd.find_element(By.CSS_SELECTOR, "#box-product .regular-price").text))
        assert_that(product_campaign_price, equal_to(web_app.wd.find_element(By.CSS_SELECTOR, "#box-product .campaign-price").text))

    def test_that_regular_price_for_product_in_campaign_is_grey_and_small_and_strike(self, web_app):
        # На главной странице
        products = web_app.list_product_cards_in_campaign_section
        product_regular_price = products[0].find_element(By.CSS_SELECTOR, ".regular-price")
        (color, size, text_style) = web_app.get_element_style(product_regular_price)
        assert_that(color, equal_to("rgba(119, 119, 119, 1)"))
        assert_that(size, equal_to("14.4px"))
        assert_that(text_style, equal_to("line-through"))
        # На странице товара
        products[0].click()
        product_regular_price = web_app.wd.find_element(By.CSS_SELECTOR, "#box-product .regular-price")
        (color, size, text_style) = web_app.get_element_style(product_regular_price)
        assert_that(color, equal_to("rgba(102, 102, 102, 1)"))
        assert_that(size, equal_to("16px"))
        assert_that(text_style, equal_to("line-through"))

    def test_that_campaign_price_for_product_in_campaign_is_red_and_big(self, web_app):
        # На главной странице
        products = web_app.list_product_cards_in_campaign_section
        product_campaign_price = products[0].find_element(By.CSS_SELECTOR, ".campaign-price")
        (color, size, text_style) = web_app.get_element_style(product_campaign_price)
        assert_that(color, equal_to("rgba(204, 0, 0, 1)"))
        assert_that(size, equal_to("18px"))
        # На странице товара
        products[0].click()
        product_campaign_price = web_app.wd.find_element(By.CSS_SELECTOR, "#box-product .campaign-price")
        (color, size, text_style) = web_app.get_element_style(product_campaign_price)
        assert_that(color, equal_to("rgba(204, 0, 0, 1)"))
        assert_that(size, equal_to("22px"))

    def test_user_can_singup_and_login_in_web_app(self, web_app):
        user = generate_random_data_for_user()
        web_app.open_page("create_account")
        web_app.fill_singup_form(firstname=user.firstname, lastname=user.lastname, address1=user.address1,
                                 postcode=user.postcode, city=user.city, country=user.country, email=user.email,
                                 phone=user.phone, password=user.password, confirmed_password=user.confirmed_password)
        web_app.click_singup()
        web_app.force_logout()
        web_app.fill_login_form(email=user.email, password=user.password)
        web_app.click_login()
        assert_that(web_app.wd.find_element(By.CSS_SELECTOR, "#notices .success").text,
                    equal_to("You are now logged in as %s %s." % (user.firstname, user.lastname)))

    def test_user_can_add_some_product_in_cart_and_then_remove_them_all_from_the_cart(self, web_app):
        for i in xrange(3):
            web_app.product_card[i].click()
            web_app.add_product_to_cart()
            web_app.open_litecart_main_page()
        web_app.open_cart()
        for i in xrange(3):
            web_app.remove_product_from_cart()
        assert_that(web_app.wd.find_element(By.CSS_SELECTOR, "#checkout-cart-wrapper").text,
                        contains_string("There are no items in your cart."))
