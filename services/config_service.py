"Configuration Service"

from utils.json_utils import get_json_file_content, validate_with_json_schema

# pylint: disable=too-few-public-methods


class ConfigService:
    "Configuration Service Class"

    def get_configs_from_file(self, file_path: str, validation_schema: dict) -> dict:
        "Gets configurations from json file"

        config_content = get_json_file_content(file_path)
        validate_with_json_schema(config_content, validation_schema)
        return config_content
