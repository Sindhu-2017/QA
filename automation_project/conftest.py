import pytest
from selenium import webdriver
from config.config import BASE_URL
@pytest.fixture
def driver():
    browser=webdriver.Chrome()

    browser.get(BASE_URL)

    yield browser

    browser.save_screenshot("automation_project.png")

    browser.quit()