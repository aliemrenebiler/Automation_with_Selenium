"Compare Omniens Product Informations With Trendyol And Hepsiburada Workflow"

from common.constants.config_schemas import (
    COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_SCHEMA,
)
from common.constants.file_and_folder_paths import (
    COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_FILE_PATH,
)
from models.account_credentials import AccountCredentials
from models.errors import ConfigError
from models.excel import ExcelCells, ExcelFile, ExcelRange
from services.config_service import ConfigService
from services.product_content_service import ProductContentService
from utils.selenium_utils import create_chrome_browser

# pylint: disable=broad-exception-caught


def _get_configs():
    configuration_service = ConfigService()
    try:
        config = configuration_service.get_configs_from_file(
            COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_FILE_PATH,
            COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_SCHEMA,
        )
        return (
            AccountCredentials(
                username=config["omniens_username"],
                password=config["omniens_password"],
            ),
            ExcelFile(
                file_path=config["excel_file_path"],
                sheet_name=config["excel_sheet_name"],
            ),
            ExcelCells(
                column=config["excel_product_codes_column"],
                row=ExcelRange(
                    start=config["excel_product_rows_start"],
                    end=config["excel_product_rows_end"],
                ),
            ),
            config["excel_trendyol_product_urls_column"],
            config["excel_hepsiburada_product_urls_column"],
        )
    except Exception as exc:
        raise ConfigError(str(exc)) from exc


def compare_product_infos_with_ty_and_hb():
    "Creates a comparison HTML file for Omniens, Trendyol and Hepsiburada"

    product_content_service = ProductContentService()
    try:
        print("Getting configurations from file...")
        (
            omniens_credentials,
            excel_file,
            excel_product_code_cells,
            excel_trendyol_product_url_column,
            excel_hepsiburada_product_url_column,
        ) = _get_configs()
        print("Opening Chrome browser...")
        browser = create_chrome_browser()
        browser.maximize_window()
        print("Getting product codes from excel file...")
        product_codes = product_content_service.get_product_codes_from_excel(
            excel_file,
            excel_product_code_cells,
        )
        print("Getting Trendyol product URLs from excel file...")
        trendyol_urls = product_content_service.get_product_urls_from_excel(
            excel_file,
            excel_product_code_cells.row,
            excel_product_code_cells.column,
            excel_trendyol_product_url_column,
        )
        print("Getting Hepsiburada product URLs from excel file...")
        hepsiburada_urls = product_content_service.get_product_urls_from_excel(
            excel_file,
            excel_product_code_cells.row,
            excel_product_code_cells.column,
            excel_hepsiburada_product_url_column,
        )
        print("Creating product information comparison HTML file...")
        product_content_service.create_product_information_comparison_html(
            browser,
            omniens_credentials,
            product_codes,
            trendyol_urls,
            hepsiburada_urls,
        )
        browser.close()
        print("Completed successfully.")
    except Exception as exc:
        print(f"Unexpected Error: {str(exc)}")
