"Omniens Utils"

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.constants.website_urls import (
    OMNIENS_LOGIN_PAGE_URL,
    OMNIENS_PRODUCTS_PAGE_URL,
    OMNIENS_DASHBOARD_PAGE_URL,
)
from models.errors import LoginError, NotFoundError, WebDriverError
from models.web_driver import WebDriver

# pylint: disable=broad-except


def login_to_omniens(
    browser: WebDriver,
    email: str,
    password: str,
    timeout: int = 10,
):
    "Logins to Omniens"

    try:
        if browser.current_url != OMNIENS_LOGIN_PAGE_URL:
            browser.get(OMNIENS_LOGIN_PAGE_URL)

        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@name="username"]',
                )
            )
        ).send_keys(email)

        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@name="pass"]',
                )
            )
        ).send_keys(password)

        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//button[@class="login100-form-btn"]',
                )
            )
        ).click()

        WebDriverWait(browser, timeout).until(EC.url_to_be(OMNIENS_DASHBOARD_PAGE_URL))
    except Exception as exc:
        raise LoginError("Could not login to Omniens.") from exc


def logged_in_to_omniens(browser: WebDriver, timeout: int = 10) -> bool:
    "Checks if still logged in to Omniens"

    try:
        browser.get(OMNIENS_PRODUCTS_PAGE_URL)
        WebDriverWait(browser, timeout).until(EC.url_to_be(OMNIENS_PRODUCTS_PAGE_URL))
        return True
    except Exception:
        return False


def get_product_info_from_omniens(
    browser: WebDriver, product_code: str, timeout: int = 10
) -> (str | None, str | None):
    "Gets the product name and description on Omniens"

    try:
        if browser.current_url != OMNIENS_PRODUCTS_PAGE_URL:
            browser.get(OMNIENS_PRODUCTS_PAGE_URL)
    except Exception as exc:
        raise WebDriverError("Could not reach Omniens product page.") from exc

    try:
        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@placeholder="anahtar kelime aratın"]')
            )
        ).send_keys(product_code, Keys.ENTER)
    except Exception as exc:
        raise WebDriverError("Could not search product on Omniens.") from exc

    action = ActionChains(browser)
    try:
        product_element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//tbody//span[normalize-space(text())="{product_code}"]')
            )
        )
        action.double_click(product_element).perform()
    except Exception as exc:
        raise NotFoundError("Product not found on Omniens.") from exc

    try:
        product_name = (
            WebDriverWait(browser, timeout)
            .until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@placeholder="Ürün Adı"]')
                )
            )
            .get_attribute("value")
        )
    except Exception:
        product_name = None

    try:
        product_desc_element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="angular-editor-textarea"]')
            )
        )

        action.move_to_element(product_desc_element).perform()
        product_desc_child_elements = product_desc_element.find_elements(By.XPATH, "*")
        product_desc = "".join(
            [
                prodct_desc_child_element.get_attribute("outerHTML")
                for prodct_desc_child_element in product_desc_child_elements
            ]
        )
    except Exception:
        product_desc = None

    return product_name, product_desc
