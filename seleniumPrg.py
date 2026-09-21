# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.google.com")
# print(driver.title)
# driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")

    yield browser

    browser.quit()


def test_title(driver):
    assert driver.title == "Example Domain"