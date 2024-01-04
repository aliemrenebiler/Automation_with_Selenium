"Excel Sheet Cell Model"

# pylint: disable=too-few-public-methods


class ExcelSheetCell:
    "Excel Sheet Cell Model Class"

    row_start: int
    column_start: int
    row_end: int | None
    column_end: int | None

    def __init__(self, row_start, column_start, row_end=None, column_end=None):
        self.row_start = row_start
        self.column_start = column_start
        self.row_end = row_end
        self.column_end = column_end
