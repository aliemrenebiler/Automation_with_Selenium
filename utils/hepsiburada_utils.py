"Hepsiburada Utils"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.web_driver import WebDriver

# pylint: disable=broad-except


def login_to_hepsiburada(
    browser: WebDriver, email: str, password: str, timeout: int = 300
):
    "Logins to Hepsiburada"

    browser.get("https://merchant.hepsiburada.com/v2/login")

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@id="username"]',
            )
        )
    ).send_keys(email)

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@id="merchant-sign-in-button"]',
            )
        )
    ).click()

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//input[@id="password"]',
            )
        )
    ).send_keys(password)

    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//button[@id="merchant-sign-in-button"]',
            )
        )
    ).click()

    WebDriverWait(browser, timeout).until(
        EC.url_to_be("https://merchant.hepsiburada.com/v2/dashboard")
        or EC.url_to_be("https://merchant.hepsiburada.com/v2/listing?tab=onSale")
    )


def get_product_url_from_hepsiburada(
    browser: WebDriver, product_code: str, timeout: int = 8
) -> str | None:
    "Gets the URL of the product with specified code from Hepsiburada"
    try:
        browser.get(
            "https://merchant.hepsiburada.com/v2/listings?"
            + f"tab=onSale&page=1&pageSize=10&search={product_code}"
        )

        try:
            WebDriverWait(browser, timeout).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//div[@class="no-data-placeholder"]',
                    )
                )
            )
            return None
        except Exception:
            ...

        product_url = (
            WebDriverWait(browser, timeout)
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//div[contains(@class, "card-text")]//a',
                    )
                )
            )
            .get_attribute("href")
        )

        return product_url
    except Exception:
        return None


def get_product_info_from_hepsiburada(
    browser: WebDriver, product_url: str, timeout: int = 10
) -> (str, str):
    "Gets the product name and description on Hepsiburada"

    browser.get(product_url)

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

    return product_name, product_desc
