"Save Trendyol Product URLs To Excel Workflow"

from common.constants.config_schemas import (
    SAVE_TY_PARTNER_PRODUCT_URLS_TO_EXCEL_CONFIG_SCHEMA,
)
from common.constants.file_and_folder_paths import (
    SAVE_TY_PARTNER_PRODUCT_URLS_TO_EXCEL_CONFIG_FILE_PATH,
)
from models.account_credentials import AccountCredentials
from models.errors import ConfigError
from models.excel import ExcelCells, ExcelFile, ExcelRange
from services.config_service import ConfigService
from services.excel_service import ExcelService
from services.product_content_service import ProductContentService
from utils.selenium_utils import create_chrome_browser

# pylint: disable=broad-exception-caught


def _get_configs():
    configuration_service = ConfigService()
    try:
        config = configuration_service.get_configs_from_file(
            SAVE_TY_PARTNER_PRODUCT_URLS_TO_EXCEL_CONFIG_FILE_PATH,
            SAVE_TY_PARTNER_PRODUCT_URLS_TO_EXCEL_CONFIG_SCHEMA,
        )
        return (
            AccountCredentials(
                username=config["trendyol_username"],
                password=config["trendyol_password"],
            ),
            ExcelFile(
                file_path=config["excel_file_path"],
                sheet_name=config["excel_sheet_name"],
            ),
            ExcelCells(
                column=config["excel_product_codes_column"],
                row=ExcelRange(
                    config["excel_product_rows_start"],
                    config["excel_product_rows_end"],
                ),
            ),
            config["excel_trendyol_product_urls_column"],
            config["excel_product_rows_start"],
        )
    except Exception as exc:
        raise ConfigError(str(exc)) from exc


def save_trendyol_partner_product_urls_to_excel():
    "Gets product codes from excel file, save Trendyol product URLs to the excel file"

    excel_service = ExcelService()
    product_content_service = ProductContentService()
    try:
        print("Getting configurations from file...")
        (
            trendyol_credentials,
            excel_file,
            excel_product_code_cells,
            excel_trendyol_product_url_column,
            excel_trendyol_product_url_row_start,
        ) = _get_configs()
        print("Opening Chrome browser...")
        browser = create_chrome_browser()
        browser.maximize_window()
        print("Getting product codes from excel file...")
        product_codes = excel_service.get_product_codes_from_excel(
            excel_file,
            excel_product_code_cells,
        )
        print("Saving Trendyol product URLs to excel...")
        product_content_service.save_trendyol_product_urls_to_excel(
            browser,
            trendyol_credentials,
            product_codes,
            excel_file,
            excel_trendyol_product_url_column,
            excel_trendyol_product_url_row_start,
        )
        browser.close()
        print("Completed successfully.")
    except Exception as exc:
        print(f"Unexpected Error: {str(exc)}")
