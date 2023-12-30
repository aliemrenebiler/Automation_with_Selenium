"""
This is an content checker for bathroom products.

- It gets the product codes from excel file,
- finds the product in multiple platforms,
- and check the product content.
"""

# pylint: disable=broad-except

from time import sleep
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------------------
# COFIGURATIONS
# ----------------------------
EXCEL_FILE_PATH = "/Users/aliemrenebiler/Desktop/vitra_temp.xlsx"
SHEET_NAME = "Sheet1"
PRODUCTS_START_ROW_NUMBER = 2
PRODUCT_CODES_COL_NUMBER = 2
PRODUCT_NAMES_COL_NUMBER = 3
WEBSITES = {
    "trendyol": {
        "name_col_number": 4,
        "desc_col_number": 5,
        "image_col_number": 6,
    },
    "hepsiburada": {
        "name_col_number": 7,
        "desc_col_number": 8,
        "image_col_number": 9,
    },
}
TIMEOUT = 3
# ----------------------------


def login_to_trendyol(browser: webdriver, email: str, password: str):
    "Logins to Trendyol"

    browser.get("https://partner.trendyol.com/account/login")

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="email-phone g-input"]//input',
            )
        )
    ).send_keys(email)

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="password g-input"]//input',
            )
        )
    ).send_keys(password)

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@class="invisible-captcha-btn btn '
                + 'btn-lg btn-mp-primary btn-block g-button -primary"]',
            )
        )
    ).click()


def login_to_hepsiburada(browser: webdriver, email: str, password: str):
    "Logins to HepsiBurada"

    browser.get("https://merchant.hepsiburada.com/v2/login")

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="input-container large"]//input',
            )
        )
    ).send_keys(email)

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@class="hb-btn large primary login-button '
                + 'new-login-button g-recaptcha "]',
            )
        )
    ).click()

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="input-container large"]//input',
            )
        )
    ).send_keys(password)

    WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@class="hb-btn large primary login-button '
                + 'new-login-button g-recaptcha "]',
            )
        )
    ).click()


def main():
    "Main code"

    # Create browser
    active_browser = webdriver.Chrome()

    login_to_trendyol(active_browser, "alemre", "123")

    sleep(5)

    active_browser.close()

    print("Completed.")


if __name__ == "__main__":
    main()
