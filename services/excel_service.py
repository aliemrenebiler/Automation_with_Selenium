"Excel Service"

from models.excel import ExcelFile, ExcelCells, ExcelRange
from utils.excel_utils import get_column_data_from_excel_sheet, open_workbook


class ExcelService:
    "Excel Service Class"

    def get_product_codes_from_excel(
        self,
        excel_file: ExcelFile,
        product_code_cells: ExcelCells,
    ):
        "Gets all product codes from specified column and in excel sheet"

        excel_file.workbook = open_workbook(excel_file.file_path)
        excel_file.sheet = excel_file.workbook[excel_file.sheet_name]

        product_codes = get_column_data_from_excel_sheet(
            excel_file.sheet,
            product_code_cells.column,
            product_code_cells.row.start,
            product_code_cells.row.end,
        )

        excel_file.workbook.close()

        return [str(product_code).strip() for product_code in product_codes]

    def get_product_urls_from_excel(
        self,
        excel_file: ExcelFile,
        product_rows: ExcelRange,
        product_code_column: int,
        product_url_column: int,
    ) -> dict:
        "Gets all product URLs from specified column and in excel sheet"

        excel_file.workbook = open_workbook(excel_file.file_path)
        excel_file.sheet = excel_file.workbook[excel_file.sheet_name]

        product_codes = get_column_data_from_excel_sheet(
            excel_file.sheet,
            product_code_column,
            product_rows.start,
            product_rows.end,
        )

        product_urls = get_column_data_from_excel_sheet(
            excel_file.sheet,
            product_url_column,
            product_rows.start,
            product_rows.end,
        )

        excel_file.workbook.close()

        return {
            str(product_code).strip(): product_urls[i]
            for i, product_code in enumerate(product_codes)
            if product_urls[i]
        }
