"File And Folder Paths"

import os

# Configuration Paths
COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_FILE_PATH = os.path.join(
    "configs",
    "compare_omniens_product_infos_with_ty_and_hb.json",
)
SAVE_TY_PARTNER_PRODUCT_URLS_TO_EXCEL_CONFIG_FILE_PATH = os.path.join(
    "configs",
    "save_trendyol_partner_product_urls_to_excel.json",
)
SAVE_HB_MERCHANT_PRODUCT_URLS_TO_EXCEL_CONFIG_FILE_PATH = os.path.join(
    "configs",
    "save_hepsiburada_merchant_product_urls_to_excel.json",
)

# Temporary Paths
TEMP_FOLDER_PATH = "temp"

# Jinja Paths
JINJA_FOLDER_PATH = os.path.join(
    "common",
    "templates",
)
PRODUCT_INFO_COMPARISON_JINJA_TEMPLATE = "product_info_comparison_jinja_template.html"
