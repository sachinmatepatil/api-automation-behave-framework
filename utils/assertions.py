# ✅ utils/assertions.py – Beginner-Friendly Explanation

import logging
import json
import os
from jsonschema import validate, ValidationError


# 🔹 This function checks if the status code of the response is what we expect.
def assert_status_code(response, expected_code):
    actual = response.status_code
    logging.info(f"Checking status code: Expected {expected_code}, Got {actual}")
    assert actual == expected_code, f"Expected status {expected_code}, but got {actual}"


# 🔹 This checks if a particular header is present in the API response.
def assert_header_present(response, header_key):
    logging.info(f"Checking if header '{header_key}' is present")
    assert header_key in response.headers, f"Header '{header_key}' not found in response"


# 🔹 This checks if all the expected keys exist in the JSON response body.
def assert_key_in_response(response, expected_keys: list):
    response_json = response.json()
    logging.info(f"Checking keys: {expected_keys}")

    if isinstance(response_json, list):
        missing_indices = [
            idx for idx, item in enumerate(response_json)
            if not isinstance(item, dict) or any(key not in item for key in expected_keys)
        ]
        assert not missing_indices, (
            f"Missing keys {expected_keys} in response items at positions {missing_indices}"
        )
    elif isinstance(response_json, dict):
        missing_keys = [key for key in expected_keys if key not in response_json]
        assert not missing_keys, f"Missing keys in response: {missing_keys}"
    else:
        raise AssertionError("Response JSON must be a list or dictionary")


# 🔹 This function checks if the structure of the response matches the schema.
# Schema is like a blueprint – it tells how the JSON should look.
def assert_schema(response_json, schema_path):
    try:
        # Join current working directory and path to schema file
        schema_file = os.path.join(os.getcwd(), schema_path)

        # Open and read the schema file (JSON format)
        with open(schema_file, 'r') as f:
            schema = json.load(f)

        # Validate response JSON using jsonschema's validate function
        validate(instance=response_json, schema=schema)
        logging.info("Schema validation passed ✅")

    except ValidationError as e:
        logging.error(f"Schema validation failed ❌: {e}")
        raise AssertionError(f"Schema validation failed: {e}")

    except Exception as e:
        raise Exception(f"Something went wrong while loading the schema file: {e}")
