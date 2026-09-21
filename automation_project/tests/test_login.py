from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest
from test_data.login_data import LOGIN_DATA
@pytest.mark.parametrize("username,password,expected_result",
    LOGIN_DATA)


def test_valid_login(driver,username,password,expected_result):

    login_page=LoginPage(driver)

    login_page.login(username,password)

    if expected_result:
        product_page=ProductsPage(driver)
        assert product_page.get_page_title() == "Products"

    else:
        assert login_page.is_login_error_displayed()


