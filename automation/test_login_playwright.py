from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch()

    page=browser.new_page()

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    products=page.get_by_text("Products")
    print(products.inner_text())

    assert products.inner_text() == "Products"

    page.screenshot(path="login_playwright.png")
    browser.close()