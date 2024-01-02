"""
This is an content checker for bathroom products.

- It gets the product codes from excel file,
- finds the product in multiple platforms,
- and check the product content.
"""

# pylint: disable=broad-except
# pylint: disable=broad-exception-raised

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.web_driver import WebDriver

# ----------------------------
# COFIGURATIONS
# ----------------------------
EXCEL_FILE_PATH = "/path/to/file.xlsx"
SHEET_NAME = "sheet_name"
PRODUCTS_START_ROW_NUMBER = 0
PRODUCT_CODES_COL_NUMBER = 0
PRODUCT_NAMES_COL_NUMBER = 0
WEBSITES = {
    "trendyol": {
        "username": "user",
        "password": "pswrd",
        "url_col_number": 0,
        "name_col_number": 0,
        "desc_col_number": 0,
        "image_col_number": 0,
        "timeout": 3,
    },
    "hepsiburada": {
        "username": "user",
        "password": "pswrd",
        "url_col_number": 0,
        "name_col_number": 0,
        "desc_col_number": 0,
        "image_col_number": 0,
        "timeout": 10,
    },
}
DEFAULT_TIMEOUT = 3
LOGIN_TIMEOUT = 300


# ----------------------------
# FOR OMNIENS
# ----------------------------
def login_to_omniens(browser: WebDriver, email: str, password: str):
    "Logins to Trendyol"

    browser.get("https://platform.omniens.com/login")

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@name="username"]',
            )
        )
    ).send_keys(email)

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@name="password"]',
            )
        )
    ).send_keys(password)

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@class="login100-form-btn"]',
            )
        )
    ).click()

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.url_to_be("https://platform.omniens.com/performance-dashboard")
    )


def get_product_info_from_omniens(browser: WebDriver, product_code: str) -> str:
    "Gets the URL of the product with specified code from Trendyol"

    browser.get("https://platform.omniens.com/_product/product/list")

    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@id="mat-input-54"]',
            )
        )
    ).send_keys(product_code, Keys.ENTER)

    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//mat-checkbox[@id="mat-checkbox-2"]',
            )
        )
    ).click()

    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//app-split-button[@class="ng-star-inserted"]',
            )
        )
    ).click()

    WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//li[@class="menuitem"]/a[text()="Düzenle"]',
            )
        )
    ).click()

    product_name = (
        WebDriverWait(browser, DEFAULT_TIMEOUT)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@id="mat-input-9"]',
                )
            )
        )
        .get_attribute("value")
    )

    product_desc = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="angular-editor-textarea"]',
            )
        )
    )

    return product_name, product_desc


# ----------------------------
# FOR TRENDYOL
# ----------------------------
def login_to_trendyol(browser: WebDriver, email: str, password: str):
    "Logins to Trendyol"

    browser.get("https://partner.trendyol.com/account/login")

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="email-phone g-input"]//input',
            )
        )
    ).send_keys(email)

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@class="password g-input"]//input',
            )
        )
    ).send_keys(password)

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@class="invisible-captcha-btn btn '
                + 'btn-lg btn-mp-primary btn-block g-button -primary"]',
            )
        )
    ).click()

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.url_to_be("https://partner.trendyol.com/dashboard")
        or EC.url_to_be(
            "https://partner.trendyol.com/account/info"
            + "?tab=contractAndDocuments&openApproveModal=true"
        )
    )


def get_product_url_from_trendyol(browser: WebDriver, product_code: str) -> str | None:
    "Gets the URL of the product with specified code from Trendyol"
    try:
        if (
            browser.current_url
            != "https://partner.trendyol.com/product-listing/all-products"
        ):
            browser.get("https://partner.trendyol.com/product-listing/all-products")

        WebDriverWait(browser, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//bl-input[@cy-id="stockCodeFilter"]',
                )
            )
        ).send_keys(product_code)

        WebDriverWait(browser, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//bl-button[@cy-id="submitFilter"]',
                )
            )
        ).click()

        product_url = (
            WebDriverWait(browser, WEBSITES["trendyol"]["timeout"])
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//sc-product-info",
                    )
                )
            )
            .get_attribute("href")
        )

        return product_url
    except Exception:
        return None


def get_product_info_from_trendyol(browser: WebDriver, product_url: str) -> (str, str):
    "Gets the product name and description on Trendyol"

    browser.get(product_url)

    product_name = (
        WebDriverWait(browser, DEFAULT_TIMEOUT)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@class="product-detail-wrapper"]//h1[@class="pr-new-br"]/span',
                )
            )
        )
        .text
    )

    product_desc_child_elements = (
        WebDriverWait(browser, DEFAULT_TIMEOUT)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@id="rich-content-wrapper"]',
                )
            )
        )
        .find_elements(By.XPATH, "*")
    )

    product_desc = "".join(
        [child.get_attribute("outerHTML") for child in product_desc_child_elements]
    )

    return product_name, product_desc


# ----------------------------
# FOR HEPSI BURADA
# ----------------------------
def login_to_hepsiburada(browser: WebDriver, email: str, password: str):
    "Logins to HepsiBurada"

    browser.get("https://merchant.hepsiburada.com/v2/login")

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@id="username"]',
            )
        )
    ).send_keys(email)

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@id="merchant-sign-in-button"]',
            )
        )
    ).click()

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@id="password"]',
            )
        )
    ).send_keys(password)

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@id="merchant-sign-in-button"]',
            )
        )
    ).click()

    WebDriverWait(browser, LOGIN_TIMEOUT).until(
        EC.url_to_be("https://merchant.hepsiburada.com/v2/dashboard")
        or EC.url_to_be("https://merchant.hepsiburada.com/v2/listing?tab=onSale")
    )


def get_product_url_from_hepsiburada(
    browser: WebDriver, product_code: str
) -> str | None:
    "Gets the URL of the product with specified code from Hepsi Burada"
    try:
        browser.get(
            "https://merchant.hepsiburada.com/v2/listings?"
            + f"tab=onSale&page=1&pageSize=10&search={product_code}"
        )

        product_url = (
            WebDriverWait(browser, WEBSITES["hepsiburada"]["timeout"])
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//div[@class="card-text two-line"]//a',
                    )
                )
            )
            .get_attribute("href")
        )

        return product_url
    except Exception:
        return None


def get_product_info_from_hepsiburada(
    browser: WebDriver, product_url: str
) -> (str, str):
    "Gets the product name and description on Hepsi Burada"

    browser.get(product_url)

    product_name = (
        WebDriverWait(browser, DEFAULT_TIMEOUT)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//h1[@id="product-name"]',
                )
            )
        )
        .text
    )

    product_desc_child_elements = (
        WebDriverWait(browser, DEFAULT_TIMEOUT)
        .until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@id="productDescriptionContent"]',
                )
            )
        )
        .find_elements(By.XPATH, "*")
    )

    product_desc = "".join(
        [child.get_attribute("outerHTML") for child in product_desc_child_elements]
    )

    return product_name, product_desc


# ----------------------------
# MAIN
# ----------------------------
def main():
    "Main code"

    # Open excel file
    workbook = load_workbook(EXCEL_FILE_PATH)
    try:
        sheet = workbook[SHEET_NAME]
    except Exception:
        sheet = workbook.active

    # Get product codes
    product_codes = [
        cell.value
        for cell in sheet[get_column_letter(PRODUCT_CODES_COL_NUMBER)][
            PRODUCTS_START_ROW_NUMBER - 1 :
        ]
    ]

    # Create browser
    active_browser = Chrome()

    # Maximize the window
    active_browser.maximize_window()

    try:
        # Login to Trendyol
        login_to_trendyol(
            active_browser,
            WEBSITES["trendyol"]["username"],
            WEBSITES["trendyol"]["password"],
        )

        # Get URLs
        for product_index, product_code in enumerate(product_codes):
            try:
                # Get Trendyol product URL
                product_url = get_product_url_from_trendyol(
                    active_browser, product_code
                )

                # Raise exception if product URL was not found
                if not product_url:
                    raise Exception(
                        f"Could not found product on Trendyol: {product_code}"
                    )

                # Add product URL to excel
                sheet[
                    get_column_letter(
                        WEBSITES["trendyol"]["url_col_number"],
                    )
                    + str(product_index + PRODUCTS_START_ROW_NUMBER)
                ] = product_url
            except Exception as error:
                print(str(error))

        # Save excel file
        workbook.save(EXCEL_FILE_PATH)

        # Login to Hepsi Burada
        login_to_hepsiburada(
            active_browser,
            WEBSITES["hepsiburada"]["username"],
            WEBSITES["hepsiburada"]["password"],
        )

        # Get URLs
        for product_index, product_code in enumerate(product_codes):
            try:
                # Get Hepsi Burada product URL
                product_url = get_product_url_from_hepsiburada(
                    active_browser, product_code
                )

                # Raise exception if product URL was not found
                if not product_url:
                    raise Exception(
                        f"Could not found product on Hepsi Burada: {product_code}"
                    )

                # Add product URL to excel
                sheet[
                    get_column_letter(
                        WEBSITES["hepsiburada"]["url_col_number"],
                    )
                    + str(product_index + PRODUCTS_START_ROW_NUMBER)
                ] = product_url
            except Exception as error:
                print(str(error))

        # Save excel file
        workbook.save(EXCEL_FILE_PATH)

    except Exception:
        print("An unexpected error occured.")

    # Close excel and browser
    workbook.close()
    active_browser.close()

    print("Completed.")


if __name__ == "__main__":
    main()
