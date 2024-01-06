"Product Content Workflows"

from models.account_credentials import AccountCredentials
from models.excel_cells import ExcelCells
from models.excel_file import ExcelFile
from services.product_content_service import ProductContentService
from utils.selenium_utils import create_chrome_browser

# pylint: disable=broad-except
# pylint: disable=too-many-instance-attributes


class ProductContentWorkflows:
    "Product Content Workflows Class"

    def __init__(self):
        self._config = {
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
        self._trendyol_credentials = AccountCredentials(
            username=self._config["credentials"]["trendyol"]["username"],
            password=self._config["credentials"]["trendyol"]["password"],
        )
        self._hepsiburada_credentials = AccountCredentials(
            username=self._config["credentials"]["hepsiburada"]["username"],
            password=self._config["credentials"]["hepsiburada"]["password"],
        )
        self._omniens_credentials = AccountCredentials(
            self._config["credentials"]["omniens"]["username"],
            self._config["credentials"]["omniens"]["password"],
        )
        self._excel_file = ExcelFile(
            file_path=self._config["excel"]["file_path"],
            sheet_name=self._config["excel"]["sheet_name"],
        )
        self._product_code_cells = ExcelCells(
            column_start=self._config["excel"]["products"]["code_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._trendyol_product_name_cells = ExcelCells(
            column_start=self._config["excel"]["trendyol"]["name_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._trendyol_product_desc_cells = ExcelCells(
            column_start=self._config["excel"]["trendyol"]["desc_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._trendyol_product_url_cells = ExcelCells(
            column_start=self._config["excel"]["trendyol"]["url_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._hepsiburada_product_name_cells = ExcelCells(
            column_start=self._config["excel"]["hepsiburada"]["name_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._hepsiburada_product_desc_cells = ExcelCells(
            column_start=self._config["excel"]["hepsiburada"]["desc_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._hepsiburada_product_url_cells = ExcelCells(
            column_start=self._config["excel"]["hepsiburada"]["url_column"],
            row_start=self._config["excel"]["products"]["row_start"],
            row_end=self._config["excel"]["products"]["row_end"],
        )
        self._pc_service = ProductContentService()

    def save_trendyol_product_urls_to_excel(self):
        "Gets product codes from excel file, save Trendyol product URLs to the excel file"

        print("Opening Chrome browser...")
        browser = create_chrome_browser()
        browser.maximize_window()
        try:
            print("Getting product codes from excel file...")
            product_codes = self._pc_service.get_product_codes_from_excel(
                self._excel_file,
                self._product_code_cells,
            )
            print("Saving Trendyol product URLs to excel...")
            self._pc_service.save_trendyol_product_urls_to_excel(
                browser,
                self._trendyol_credentials,
                self._excel_file,
                self._trendyol_product_url_cells,
                product_codes,
            )
            print("Completed successfully.")
        except Exception as exc:
            print(f"Unexpected Error: {str(exc)}")
        browser.close()
        print("End of workflow.")

    def save_hepsiburada_product_urls_to_excel(self):
        "Gets product codes from excel file, save Hepsiburada product URLs to the excel file"

        print("Opening Chrome browser...")
        browser = create_chrome_browser()
        browser.maximize_window()
        try:
            print("Getting product codes from excel file...")
            product_codes = self._pc_service.get_product_codes_from_excel(
                self._excel_file,
                self._product_code_cells,
            )
            print("Saving Trendyol product URLs to excel...")
            self._pc_service.save_hepsiburada_product_urls_to_excel(
                browser,
                self._hepsiburada_credentials,
                self._excel_file,
                self._hepsiburada_product_url_cells,
                product_codes,
            )
            print("Completed successfully.")
        except Exception as exc:
            print(f"Unexpected Error: {str(exc)}")
        browser.close()
        print("End of workflow.")

    def compare_product_information(self):
        "Gets product codes from excel file, save Hepsiburada product URLs to the excel file"

        print("Opening Chrome browser...")
        browser = create_chrome_browser()
        browser.maximize_window()
        try:
            print("Getting product codes from excel file...")
            product_codes = self._pc_service.get_product_codes_from_excel(
                self._excel_file,
                self._product_code_cells,
            )
            print("Getting Trendyol product URLs from excel file...")
            trendyol_urls = self._pc_service.get_product_urls_from_excel(
                self._excel_file,
                self._product_code_cells,
                self._trendyol_product_url_cells.column_start,
            )
            print("Getting Hepsiburada product URLs from excel file...")
            hepsiburada_urls = self._pc_service.get_product_urls_from_excel(
                self._excel_file,
                self._product_code_cells,
                self._hepsiburada_product_url_cells.column_start,
            )
            print("Creating product information comparison HTML file...")
            self._pc_service.create_product_information_comparison_html(
                browser,
                self._omniens_credentials,
                product_codes,
                trendyol_urls,
                hepsiburada_urls,
            )
            print("Completed successfully.")
        except Exception as exc:
            print(f"Unexpected Error: {str(exc)}")
        browser.close()
        print("End of workflow.")
