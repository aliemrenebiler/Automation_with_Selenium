"""
This is an content checker for bathroom products.

- It gets the product codes from excel file,
- finds the product in multiple platforms,
- and check the product content.
"""

# pylint: disable=broad-except
# pylint: disable=broad-exception-raised

from selenium.webdriver import Chrome, ChromeOptions
from models.account_credentials import AccountCredentials
from models.excel_cells import ExcelCells
from models.excel_file import ExcelFile
from services.product_content_service import ProductContentService

# ----------------------------
# COFIGURATIONS
# ----------------------------
CONFIG = {
    "credentials": {
        "omniens": {
            "username": "",
            "password": "",
        },
        "trendyol": {
            "username": "",
            "password": "",
        },
        "hepsiburada": {
            "username": "",
            "password": "",
        },
    },
    "excel": {
        "file_path": "",
        "sheet_name": "",
        "products": {
            "code_column": 0,
            "name_column": 0,
            "row_start": 0,
            "row_end": 0,
        },
        "trendyol": {
            "url_column": 0,
            "name_column": 0,
            "desc_column": 0,
            "image_column": 0,
        },
        "hepsiburada": {
            "url_column": 0,
            "name_column": 0,
            "desc_column": 0,
            "image_column": 0,
        },
    },
}

# ----------------------------
# CREDENTIALS
# ----------------------------
trendyol_credentials = AccountCredentials(
    username=CONFIG["credentials"]["trendyol"]["username"],
    password=CONFIG["credentials"]["trendyol"]["password"],
)
hepsiburada_credentials = AccountCredentials(
    username=CONFIG["credentials"]["hepsiburada"]["username"],
    password=CONFIG["credentials"]["hepsiburada"]["password"],
)
omniens_credentials = AccountCredentials(
    CONFIG["credentials"]["omniens"]["username"],
    CONFIG["credentials"]["omniens"]["password"],
)

# ----------------------------
# EXCEL FILE
# ----------------------------
excel_file = ExcelFile(
    file_path=CONFIG["excel"]["file_path"],
    sheet_name=CONFIG["excel"]["sheet_name"],
)

# ----------------------------
# EXCEL CELLS
# ----------------------------
product_code_cells = ExcelCells(
    column_start=CONFIG["excel"]["products"]["code_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)
trendyol_product_name_cells = ExcelCells(
    column_start=CONFIG["excel"]["trendyol"]["name_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)
trendyol_product_desc_cells = ExcelCells(
    column_start=CONFIG["excel"]["trendyol"]["desc_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)
trendyol_product_url_cells = ExcelCells(
    column_start=CONFIG["excel"]["trendyol"]["url_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)
hepsiburada_product_name_cells = ExcelCells(
    column_start=CONFIG["excel"]["hepsiburada"]["name_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)
hepsiburada_product_desc_cells = ExcelCells(
    column_start=CONFIG["excel"]["hepsiburada"]["desc_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)
hepsiburada_product_url_cells = ExcelCells(
    column_start=CONFIG["excel"]["hepsiburada"]["url_column"],
    row_start=CONFIG["excel"]["products"]["row_start"],
    row_end=CONFIG["excel"]["products"]["row_end"],
)


def main():
    "Main code"

    pc_service = ProductContentService()

    product_codes = pc_service.get_product_codes_from_excel(
        excel_file,
        product_code_cells,
    )

    options = ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    browser = Chrome(options=options)
    browser.maximize_window()

    try:
        trendyol_product_urls = pc_service.save_trendyol_product_urls_to_excel(
            browser,
            trendyol_credentials,
            excel_file,
            trendyol_product_url_cells,
            product_codes,
        )

        hepsiburada_product_urls = pc_service.save_hepsiburada_product_urls_to_excel(
            browser,
            hepsiburada_credentials,
            excel_file,
            hepsiburada_product_url_cells,
            product_codes,
        )

        pc_service.compare_product_info(
            browser,
            omniens_credentials,
            product_codes,
            trendyol_product_urls,
            hepsiburada_product_urls,
        )
    except Exception:
        print("An unexpected error occured.")

    print("Completed.")

    browser.close()


if __name__ == "__main__":
    main()
