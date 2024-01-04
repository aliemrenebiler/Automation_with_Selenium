"Product Content Service"

from models.web_driver import WebDriver

from utils.hepsiburada_utils import (
    get_product_url_from_hepsiburada,
    login_to_hepsiburada,
)
from utils.trendyol_utils import get_product_url_from_trendyol, login_to_trendyol


class ProductContentService:
    "Product Content Service Class"

    def get_product_urls_from_trendyol(
        self, browser: WebDriver, username: str, password: str, product_codes: [str]
    ):
        "Gets the product URLs from Trendyol and saves them to excel file"

        # Login
        login_to_trendyol(
            browser,
            username,
            password,
        )

        product_urls = []

        # Get URLs
        for product_code in product_codes:
            # Get product URL
            product_url = get_product_url_from_trendyol(browser, product_code)

            # Add product if product URL was found
            if product_url:
                product_urls.append(product_url)
            else:
                product_urls.append(None)
                print(f"Could not found product on Trendyol: {product_code}")

        return product_urls

    def get_product_urls_from_hepsiburada(
        self, browser: WebDriver, username: str, password: str, product_codes: [str]
    ):
        "Gets the product URLs from Hepsi Burada and saves them to excel file"

        # Login
        login_to_hepsiburada(
            browser,
            username,
            password,
        )

        product_urls = []

        # Get URLs
        for product_code in product_codes:
            # Get product URL
            product_url = get_product_url_from_hepsiburada(browser, product_code)

            # Add product if product URL was found
            if product_url:
                product_urls.append(product_url)
            else:
                product_urls.append(None)
                print(f"Could not found product on Hepsi Burada: {product_code}")

        return product_urls
