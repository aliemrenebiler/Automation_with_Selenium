"Configuration Schemas"

GLOBAL_PARAMETERS_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "timeout": {"type": "integer"},
        "login_timeout": {"type": "integer"},
    },
    "required": [
        "timeout",
        "login_timeout",
    ],
}

COMPARE_OMNIENS_PRODUCT_INFOS_WITH_TY_AND_HB_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "omniens_username": {"type": "string"},
        "omniens_password": {"type": "string"},
        "excel_file_path": {"type": "string"},
        "excel_sheet_name": {"type": "string"},
        "excel_product_codes_column": {"type": "integer"},
        "excel_trendyol_product_urls_column": {"type": "integer"},
        "excel_hepsiburada_product_urls_column": {"type": "integer"},
        "excel_product_rows_start": {"type": "integer"},
        "excel_product_rows_end": {"type": "integer"},
    },
    "required": [
        "omniens_username",
        "omniens_password",
        "excel_file_path",
        "excel_sheet_name",
        "excel_product_codes_column",
        "excel_trendyol_product_urls_column",
        "excel_hepsiburada_product_urls_column",
        "excel_product_rows_start",
        "excel_product_rows_end",
    ],
}

SAVE_TY_PARTNER_PRODUCT_URLS_TO_EXCEL_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "trendyol_username": {"type": "string"},
        "trendyol_password": {"type": "string"},
        "excel_file_path": {"type": "string"},
        "excel_sheet_name": {"type": "string"},
        "excel_product_codes_column": {"type": "integer"},
        "excel_trendyol_product_urls_column": {"type": "integer"},
        "excel_product_rows_start": {"type": "integer"},
        "excel_product_rows_end": {"type": "integer"},
    },
    "required": [
        "trendyol_username",
        "trendyol_password",
        "excel_file_path",
        "excel_sheet_name",
        "excel_product_codes_column",
        "excel_trendyol_product_urls_column",
        "excel_product_rows_start",
        "excel_product_rows_end",
    ],
}

SAVE_HB_MERCHANT_PRODUCT_URLS_TO_EXCEL_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "hepsiburada_username": {"type": "string"},
        "hepsiburada_password": {"type": "string"},
        "excel_file_path": {"type": "string"},
        "excel_sheet_name": {"type": "string"},
        "excel_product_codes_column": {"type": "integer"},
        "excel_hepsiburada_product_urls_column": {"type": "integer"},
        "excel_product_rows_start": {"type": "integer"},
        "excel_product_rows_end": {"type": "integer"},
    },
    "required": [
        "hepsiburada_username",
        "hepsiburada_password",
        "excel_file_path",
        "excel_sheet_name",
        "excel_product_codes_column",
        "excel_hepsiburada_product_urls_column",
        "excel_product_rows_start",
        "excel_product_rows_end",
    ],
}

SAVE_OMNIENS_PRODUCT_NAMES_TO_EXCEL_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "omniens_username": {"type": "string"},
        "omniens_password": {"type": "string"},
        "excel_file_path": {"type": "string"},
        "excel_sheet_name": {"type": "string"},
        "excel_product_codes_column": {"type": "integer"},
        "excel_omniens_product_names_column": {"type": "integer"},
        "excel_product_rows_start": {"type": "integer"},
        "excel_product_rows_end": {"type": "integer"},
    },
    "required": [
        "omniens_username",
        "omniens_password",
        "excel_file_path",
        "excel_sheet_name",
        "excel_product_codes_column",
        "excel_omniens_product_names_column",
        "excel_product_rows_start",
        "excel_product_rows_end",
    ],
}
