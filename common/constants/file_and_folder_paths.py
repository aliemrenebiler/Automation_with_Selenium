"File Paths"

import os

# Configuration Paths
COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_FILE_PATH = os.path.join(
    "config",
    "workflow_configs",
    "compare_omniens_product_infos_with_ty_and_hb.json",
)
SAVE_TRENDYOL_PRODUCT_URLS_TO_EXCEL_CONFIG_FILE_PATH = os.path.join(
    "config",
    "workflow_configs",
    "save_trendyol_product_urls_to_excel.json",
)
SAVE_HEPSIBURADA_PRODUCT_URLS_TO_EXCEL_CONFIG_FILE_PATH = os.path.join(
    "config",
    "workflow_configs",
    "save_hepsiburada_product_urls_to_excel.json",
)

# Temporary Paths
TEMP_FOLDER_PATH = "temp"

# Jinja Paths
JINJA_FOLDER_PATH = os.path.join(
    "templates",
    "jinja",
)
PRODUCT_DESC_COMPARISON_JINJA_TEMPLATE = "product_desc_comparison.html"
