import json
from behave import given, when, then
from config import BASE_URL
from utils.request_helper import APIRequest
from utils.api_helper import get_with_retry, post_with_retry

from utils.assertions import (
    assert_status_code,
    assert_schema,
    assert_header_present,
    assert_key_in_response
)


# @given('the API base URL is set')
# def step_set_base_url(context):
#     context.base_url = BASE_URL


# @when('I send a GET request to "{endpoint}"')
# def step_send_get_request(context, endpoint):
#     url = f"{context.base_url}{endpoint}"
#     context.response = APIRequest.get(url)


@then('the response status code should be 404')
def step_validation_status_code(context):
    assert context.response.status_code == 404, \
        f"Expected 200 but got {context.response.status_code}"


@then('the response should contain an error message or be empty')
def step_verify_error_message(context):
    body = context.response.text.strip().lower()
    assert body in ("", "not found", "error"), (
        f"Unexpected body for 404: {body}'"
    )
