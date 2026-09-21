from selenium.webdriver.common.by import By

class ProductsPage:

    def __init__(self,driver):
        self.driver=driver
    page_title=(By.CLASS_NAME,"title")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text