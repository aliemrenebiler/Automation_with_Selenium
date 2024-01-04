"""
This is an content checker for bathroom products.

- It gets the product codes from excel file,
- finds the product in multiple platforms,
- and check the product content.
"""

# pylint: disable=broad-except
# pylint: disable=broad-exception-raised

from selenium.webdriver import Chrome
from models.account_credentials import AccountCredentials
from models.excel_cells import ExcelCells
from models.excel_file import ExcelFile
from services.product_content_service import ProductContentService
from utils.excel_utils import (
    get_column_data_from_excel_sheet,
    open_workbook,
)

# ----------------------------
# COFIGURATIONS
# ----------------------------
EXCEL_FILE_PATH = "/path/to/file.xlsx"
SHEET_NAME = "sheet_name"
PRODUCTS_ROW_NUMBER_START = 0
PRODUCTS_ROW_NUMBER_END = 0
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
    },
    "hepsiburada": {
        "username": "user",
        "password": "pswrd",
        "url_col_number": 0,
        "name_col_number": 0,
        "desc_col_number": 0,
        "image_col_number": 0,
    },
}

excel_file = ExcelFile(
    file_path=EXCEL_FILE_PATH,
    sheet_name=SHEET_NAME,
)

product_code_cells = ExcelCells(
    column_start=PRODUCT_CODES_COL_NUMBER,
    row_start=PRODUCTS_ROW_NUMBER_START,
    row_end=PRODUCTS_ROW_NUMBER_END,
)

trendyol_credentials = AccountCredentials(
    username=WEBSITES["trendyol"]["username"],
    password=WEBSITES["trendyol"]["password"],
)

trendyol_product_url_cells = ExcelCells(
    column_start=WEBSITES["trendyol"]["url_col_number"],
    row_start=PRODUCTS_ROW_NUMBER_START,
)

hepsiburada_credentials = AccountCredentials(
    username=WEBSITES["hepsiburada"]["username"],
    password=WEBSITES["hepsiburada"]["password"],
)

hepsiburada_product_url_cells = ExcelCells(
    column_start=WEBSITES["hepsiburada"]["url_col_number"],
    row_start=PRODUCTS_ROW_NUMBER_START,
)


def main():
    "Main code"

    product_content_service = ProductContentService()

    workbook = open_workbook(EXCEL_FILE_PATH)
    sheet = workbook[SHEET_NAME]

    product_codes = get_column_data_from_excel_sheet(
        sheet,
        product_code_cells.column_start,
        product_code_cells.row_start,
        product_code_cells.row_end,
    )

    browser = Chrome()
    browser.maximize_window()

    try:
        trendyol_product_urls = (
            product_content_service.save_trendyol_product_urls_to_excel(
                browser,
                trendyol_credentials,
                excel_file,
                trendyol_product_url_cells,
                product_codes,
            )
        )

        hepsiburada_product_urls = (
            product_content_service.save_hepsiburada_product_urls_to_excel(
                browser,
                hepsiburada_credentials,
                excel_file,
                hepsiburada_product_url_cells,
                product_codes,
            )
        )

    except Exception:
        print("An unexpected error occured.")

    workbook.close()
    browser.close()

    print("Completed.")


if __name__ == "__main__":
    main()
