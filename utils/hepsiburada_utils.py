"Hepsiburada Utils"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.constants.website_urls import (
    HEPSIBURADA_MAIN_PAGE_URL,
    HEPSIBURADA_MERCHANT_DASHBOARD_PAGE_URL,
    HEPSIBURADA_MERCHANT_LOGIN_PAGE_URL,
    HEPSIBURADA_MERCHANT_PRODUCT_SEARCH_URL_TEMPLATE,
    HEPSIBURADA_MERCHANT_REDIRECT_AFTER_LOGIN_PAGE_URL,
)
from models.errors import LoginError, WebDriverError
from models.web_driver import WebDriver

# pylint: disable=broad-except


def login_to_hepsiburada(
    browser: WebDriver, email: str, password: str, timeout: int = 300
):
    "Logins to Hepsiburada"

    try:
        if browser.current_url != HEPSIBURADA_MERCHANT_LOGIN_PAGE_URL:
            browser.get(HEPSIBURADA_MERCHANT_LOGIN_PAGE_URL)

        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@id="username"]',
                )
            )
        ).send_keys(email)

        login_button_element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//button[@id="merchant-sign-in-button"]',
                )
            )
        )
        login_button_element.click()
        login_button_element.click()

        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@id="password"]',
                )
            )
        ).send_keys(password)

        login_button_element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//button[@id="merchant-sign-in-button"]',
                )
            )
        )
        login_button_element.click()
        login_button_element.click()

        WebDriverWait(browser, timeout).until(
            EC.url_to_be(HEPSIBURADA_MERCHANT_DASHBOARD_PAGE_URL)
            or EC.url_to_be(HEPSIBURADA_MERCHANT_REDIRECT_AFTER_LOGIN_PAGE_URL)
        )
    except Exception as exc:
        raise LoginError("Could not login to Hepsiburada.") from exc


def accept_hepsiburada_cookies(browser: WebDriver, timeout: int = 10):
    "Accepts Hepsiburada cookies"

    try:
        if browser.current_url != HEPSIBURADA_MAIN_PAGE_URL:
            browser.get(HEPSIBURADA_MAIN_PAGE_URL)

        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//button[@id="onetrust-accept-btn-handler"]',
                )
            )
        ).click()
    except Exception as exc:
        raise WebDriverError("Error during accepting Hepsiburada cookies.") from exc


def get_product_url_from_hepsiburada(
    browser: WebDriver, product_code: str, timeout: int = 10
) -> str | None:
    "Gets the URL of the product with specified code from Hepsiburada"

    product_search_url = HEPSIBURADA_MERCHANT_PRODUCT_SEARCH_URL_TEMPLATE.format(
        product_code
    )
    try:
        if browser.current_url != product_search_url:
            browser.get(product_search_url)
    except Exception as exc:
        raise WebDriverError(
            "Could not found Hepsiburada merchant products page."
        ) from exc

    try:
        product_url = (
            WebDriverWait(browser, timeout)
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//div[contains(@class, "card-text")]//a | //div[@class="no-data-placeholder"]',
                    )
                )
            )
            .get_attribute("href")
        )
    except Exception:
        product_url = None

    return product_url


def get_product_info_from_hepsiburada(
    browser: WebDriver, product_url: str, timeout: int = 10
) -> (str | None, str | None):
    "Gets the product name and description on Hepsiburada"

    try:
        if browser.current_url != product_url:
            browser.get(product_url)
    except Exception as exc:
        raise WebDriverError(
            "Could not get product information, could not reach Hepsiburada product page."
        ) from exc

    try:
        product_name = (
            WebDriverWait(browser, timeout)
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
    except Exception:
        product_name = None

    try:
        product_desc_child_elements = (
            WebDriverWait(browser, timeout)
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
    except Exception:
        product_desc = None

    return product_name, product_desc
