"Product Content Service"

from openpyxl.utils import get_column_letter
from models.web_driver import WebDriver
from utils.excel_utils import open_workbook

from utils.hepsiburada_utils import (
    get_product_url_from_hepsiburada,
    login_to_hepsiburada,
)
from utils.trendyol_utils import get_product_url_from_trendyol, login_to_trendyol


class ProductContentService:
    "Product Content Service Class"

    def save_trendyol_product_urls_to_excel(
        self,
        browser: WebDriver,
        trendyol_username: str,
        trendyol_password: str,
        product_codes: [str],
        excel_file_path: str,
        sheet_name: str,
        col_number: int,
        row_number_start: int,
    ) -> [str]:
        "Gets the product URLs from Trendyol and saves them to excel file"

        workbook = open_workbook(excel_file_path)
        sheet = workbook[sheet_name]
        product_urls = []

        login_to_trendyol(browser, trendyol_username, trendyol_password)
        for i, product_code in enumerate(product_codes):
            product_url = get_product_url_from_trendyol(browser, product_code)
            product_urls.append(product_url)
            if product_url:
                sheet[
                    f"{get_column_letter(col_number)}{row_number_start + i}"
                ] = product_url
                print(f"{i} - {product_code} - Trendyol URL: {product_url}")
            else:
                sheet[f"{get_column_letter(col_number)}{row_number_start + i}"] = ""
                print(f"{i} - {product_code} - Could not found product on Trendyol")
            workbook.save(excel_file_path)

        browser.close()
        workbook.close()

        return product_urls

    def save_hepsiburada_product_urls_to_excel(
        self,
        browser: WebDriver,
        trendyol_username: str,
        trendyol_password: str,
        product_codes: [str],
        excel_file_path: str,
        sheet_name: str,
        col_number: int,
        row_number_start: int,
    ) -> [str]:
        "Gets the product URLs from Hepsiburada and saves them to excel file"

        workbook = open_workbook(excel_file_path)
        sheet = workbook[sheet_name]
        product_urls = []

        login_to_hepsiburada(browser, trendyol_username, trendyol_password)
        for i, product_code in enumerate(product_codes):
            product_url = get_product_url_from_hepsiburada(browser, product_code)
            product_urls.append(product_url)
            if product_url:
                sheet[
                    f"{get_column_letter(col_number)}{row_number_start + i}"
                ] = product_url
                print(f"{i} - {product_code} - Hepsiburada URL: {product_url}")
            else:
                sheet[f"{get_column_letter(col_number)}{row_number_start + i}"] = ""
                print(f"{i} - {product_code} - Could not found product on Hepsiburada")
            workbook.save(excel_file_path)

        browser.close()
        workbook.close()

        return product_urls
