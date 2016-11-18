# -*- coding: utf-8 -*-
import pytest

def test_user_can_open_traning_page(app):
    app.wd.get('http://www.software-testing.ru/trainings/')

