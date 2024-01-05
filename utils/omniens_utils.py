"Omniens Utils"

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.web_driver import WebDriver

# pylint: disable=broad-except


def login_to_omniens(browser: WebDriver, email: str, password: str, timeout: int = 300):
    "Logins to Trendyol"

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


def get_product_info_from_omniens(
    browser: WebDriver, product_code: str, timeout: int = 10
) -> (str, str | None):
    "Gets the URL of the product with specified code from Trendyol"

    browser.get("https://platform.omniens.com/_product/product/list")

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@placeholder="anahtar kelime aratın"]',
            )
        )
    ).send_keys(product_code, Keys.ENTER)

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f'//tbody//span[contains(text(), "{product_code}")]',
            )
        )
    )

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//tbody[@role="rowgroup"]//app-checkbox',
            )
        )
    ).click()

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//app-split-button[@class="ng-star-inserted"]',
            )
        )
    ).click()

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//li[@role="menuitem"]/a[text()="Düzenle"]',
            )
        )
    ).click()

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
