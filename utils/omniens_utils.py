"Omniens Utils"

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.errors import LoginError, WebDriverError

from models.web_driver import WebDriver

# pylint: disable=broad-except


def login_to_omniens(browser: WebDriver, email: str, password: str, timeout: int = 300):
    "Logins to Omniens"

    try:
        browser.get("https://platform.omniens.com/login")

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

        WebDriverWait(browser, timeout).until(
            EC.url_to_be("https://platform.omniens.com/performance-dashboard")
        )
    except Exception as exc:
        raise LoginError("Could not login to Omniens.") from exc


def logged_in_to_omniens(browser: WebDriver, timeout: int = 10) -> bool:
    "Checks if still logged in to Omniens"

    products_page_url = "https://platform.omniens.com/_product/product/list"
    try:
        browser.get(products_page_url)
        WebDriverWait(browser, timeout).until(EC.url_to_be(products_page_url))
        return True
    except Exception:
        return False


def get_product_info_from_omniens(
    browser: WebDriver, product_code: str, timeout: int = 10
) -> (str | None, str | None):
    "Gets the product name and description on Omniens"

    products_page_url = "https://platform.omniens.com/_product/product/list"
    try:
        if browser.current_url != products_page_url:
            browser.get(products_page_url)
    except Exception as exc:
        raise WebDriverError(
            "Could not get product information, could not reach Omniens product page."
        ) from exc

    try:
        WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//input[@placeholder="anahtar kelime aratın"]',
                )
            )
        ).send_keys(product_code, Keys.ENTER)

        product_element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f'//tbody//span[contains(text(), "{product_code}")]',
                )
            )
        )
        action = ActionChains(browser)
        action.double_click(product_element).perform()
    except Exception as exc:
        raise WebDriverError("Could not get product element on Omniens.") from exc

    try:
        product_name = (
            WebDriverWait(browser, timeout)
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//input[@placeholder="Ürün Adı"]',
                    )
                )
            )
            .get_attribute("value")
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
                        '//div[@class="angular-editor-textarea"]',
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
