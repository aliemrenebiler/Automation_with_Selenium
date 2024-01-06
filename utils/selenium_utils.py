"Selenium Utils"

from selenium.webdriver import Chrome, ChromeOptions


def create_chrome_browser() -> Chrome:
    "Creates a Chrome web browser"

    options = ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    browser = Chrome(options=options)
    return browser
