"Excel Models"

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# pylint: disable=too-few-public-methods


class ExcelRange:
    "Excel Range Model Class"

    def __init__(
        self,
        start: int,
        end: int,
    ):
        self.start = start
        self.end = end


class ExcelCells:
    "Excel Cells Model Class"

    def __init__(
        self,
        row: int | ExcelRange,
        column: int | ExcelRange,
    ):
        self.row = row
        self.column = column


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
