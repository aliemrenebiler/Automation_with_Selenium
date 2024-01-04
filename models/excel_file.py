"Excel File Model"

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# pylint: disable=too-few-public-methods


class ExcelFile:
    "Excel File Model Class"

    file_path: str
    sheet_name: str | None
    workbook: Workbook | None
    sheet: Worksheet | None

    def __init__(self, file_path, sheet_name=None, workbook=None, sheet=None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = workbook
        self.sheet = sheet
