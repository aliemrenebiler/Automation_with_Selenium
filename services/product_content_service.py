"Product Content Service"

from openpyxl.utils import get_column_letter
from models.account_credentials import AccountCredentials
from models.excel_cells import ExcelCells
from models.excel_file import ExcelFile
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
        trendyol_credentials: AccountCredentials,
        excel_file: ExcelFile,
        product_cells: ExcelCells,
        product_codes: [str],
    ) -> [str]:
        "Gets the product URLs from Trendyol and saves them to excel file"

        excel_file.workbook = open_workbook(excel_file.file_path)
        excel_file.sheet = excel_file.workbook[excel_file.sheet_name]
        product_urls = []

        login_to_trendyol(
            browser,
            trendyol_credentials.username,
            trendyol_credentials.password,
        )
        for i, product_code in enumerate(product_codes):
            product_url = get_product_url_from_trendyol(browser, product_code)
            product_urls.append(product_url)
            if product_url:
                excel_file.sheet[
                    f"{get_column_letter(product_cells.column_start)}{product_cells.row_start + i}"
                ] = product_url
                print(f"{i} - {product_code} - Trendyol URL: {product_url}")
            else:
                excel_file.sheet[
                    f"{get_column_letter(product_cells.column_start)}{product_cells.row_start + i}"
                ] = ""
                print(f"{i} - {product_code} - Could not found product on Trendyol")
            excel_file.workbook.save(excel_file.file_path)
        excel_file.workbook.close()

        return product_urls

    def save_hepsiburada_product_urls_to_excel(
        self,
        browser: WebDriver,
        hepsiburada_credentials: AccountCredentials,
        excel_file: ExcelFile,
        product_cells: ExcelCells,
        product_codes: [str],
    ) -> [str]:
        "Gets the product URLs from Hepsiburada and saves them to excel file"

        excel_file.workbook = open_workbook(excel_file.file_path)
        excel_file.sheet = excel_file.workbook[excel_file.sheet_name]
        product_urls = []

        login_to_hepsiburada(
            browser,
            hepsiburada_credentials.username,
            hepsiburada_credentials.password,
        )
        for i, product_code in enumerate(product_codes):
            product_url = get_product_url_from_hepsiburada(browser, product_code)
            product_urls.append(product_url)
            if product_url:
                excel_file.sheet[
                    f"{get_column_letter(product_cells.column_start)}{product_cells.row_start + i}"
                ] = product_url
                print(f"{i} - {product_code} - Hepsiburada URL: {product_url}")
            else:
                excel_file.sheet[
                    f"{get_column_letter(product_cells.column_start)}{product_cells.row_start + i}"
                ] = ""
                print(f"{i} - {product_code} - Could not found product on Hepsiburada")
            excel_file.workbook.save(excel_file.file_path)
        excel_file.workbook.close()

        return product_urls
