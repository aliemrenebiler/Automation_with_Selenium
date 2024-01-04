"""
This is an content checker for bathroom products.

- It gets the product codes from excel file,
- finds the product in multiple platforms,
- and check the product content.
"""

# pylint: disable=broad-except
# pylint: disable=broad-exception-raised

from selenium.webdriver import Chrome
from services.product_content_service import ProductContentService
from utils.excel_utils import (
    add_data_to_excel_sheet_column,
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


# ----------------------------
# MAIN
# ----------------------------
def main():
    "Main code"

    product_content_service = ProductContentService()

    workbook = open_workbook(EXCEL_FILE_PATH)
    sheet = workbook[SHEET_NAME]

    product_codes = get_column_data_from_excel_sheet(
        sheet,
        PRODUCT_CODES_COL_NUMBER,
        PRODUCTS_ROW_NUMBER_START,
        PRODUCTS_ROW_NUMBER_END,
    )

    browser = Chrome()
    browser.maximize_window()

    try:
        trendyol_product_urls = product_content_service.get_product_urls_from_trendyol(
            browser,
            WEBSITES["trendyol"]["username"],
            WEBSITES["trendyol"]["password"],
            product_codes,
        )

        add_data_to_excel_sheet_column(
            sheet,
            WEBSITES["trendyol"]["url_col_number"],
            PRODUCTS_ROW_NUMBER_START,
            trendyol_product_urls,
        )
        workbook.save(EXCEL_FILE_PATH)

        hepsiburada_product_urls = (
            product_content_service.get_product_urls_from_hepsiburada(
                browser,
                WEBSITES["hepsiburada"]["username"],
                WEBSITES["hepsiburada"]["password"],
                product_codes,
            )
        )

        add_data_to_excel_sheet_column(
            sheet,
            WEBSITES["hepsiburada"]["url_col_number"],
            PRODUCTS_ROW_NUMBER_START,
            hepsiburada_product_urls,
        )
        workbook.save(EXCEL_FILE_PATH)

    except Exception:
        print("An unexpected error occured.")

    workbook.close()
    browser.close()

    print("Completed.")


if __name__ == "__main__":
    main()
