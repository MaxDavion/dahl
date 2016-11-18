# -*- coding: utf-8 -*-
import pytest
from app import Application



_browser = None

@pytest.yield_fixture
def app (request):
    global _browser
    if _browser is None:
        _browser = Application()
    yield _browser


@pytest.yield_fixture(scope = "class", autouse = True)
def teardown(request):
    yield teardown
    global _browser
    if _browser:
        _browser.quit()
        _browser = None
