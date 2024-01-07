"JSON Utils"

import json

from jsonschema import validate


def get_json_file_content(file_path: str) -> dict:
    "Gets JSON file content and return it as dictionary"

    with open(file_path, "r", encoding="utf8") as file:
        return json.load(file)


def validate_with_json_schema(content: dict, schema: dict):
    "Validates dictionary with JSON schema"

    validate(content, schema)
