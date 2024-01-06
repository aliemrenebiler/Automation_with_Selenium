"Excel File Model"

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# pylint: disable=too-few-public-methods


class ExcelFile:
    "Excel File Model Class"

    def __init__(
        self,
        file_path: str,
        sheet_name: str | None = None,
        workbook: Workbook | None = None,
        sheet: Worksheet | None = None,
    ):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = workbook
        self.sheet = sheet
