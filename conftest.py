# -*- coding: utf-8 -*-
import pytest
from app import AdminApp, WebApp
import os


_browser = None


@pytest.yield_fixture
def admin_app(request):
    global _browser
    if _browser is None:
        _browser = AdminApp()
        _browser.open_litecart_admin()
    yield _browser


@pytest.yield_fixture
def web_app(request):
    global _browser
    if _browser is None:
        _browser = WebApp()
        _browser.open_litecart_web()
    yield _browser


@pytest.yield_fixture(autouse = True)
def teardown(request):
    yield teardown
    global _browser
    if _browser:
        _browser.quit()
        _browser = None


def path():
    return os.path.dirname(os.path.abspath(__file__))
