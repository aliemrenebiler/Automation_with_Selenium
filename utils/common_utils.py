"Common Utils"

from datetime import datetime


def create_timestamp() -> str:
    "Creates string timestamp as <year>-<month>-<day>_<hour>-<min>-<sec>"

    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")
