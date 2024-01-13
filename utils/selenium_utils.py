"Selenium Utils"

from selenium.webdriver import Chrome, ChromeOptions


def create_chrome_browser() -> Chrome:
    "Creates a Chrome web browser"

    prefs = {"profile.default_content_setting_values.notifications": 2}

    options = ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_experimental_option("prefs", prefs)

    browser = Chrome(options=options)

    return browser
