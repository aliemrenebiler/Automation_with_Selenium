"Excel Cells Model"

# pylint: disable=too-few-public-methods


class ExcelCells:
    "Excel Cells Model Class"

    def __init__(
        self,
        row_start: int,
        column_start: int,
        row_end: int | None = None,
        column_end: int | None = None,
    ):
        self.row_start = row_start
        self.column_start = column_start
        self.row_end = row_end
        self.column_end = column_end
