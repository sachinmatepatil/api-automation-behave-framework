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


@given('the API base URL is set')
def step_set_base_url(context):
    context.base_url = BASE_URL


@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.response = APIRequest.get(url)
    context.response = get_with_retry(url)


@when('I send a GET request to booking from "{data_file}"')
def step_external_data(context, data_file):
    with open(data_file, 'r') as file:
        b_id = json.load(file)

    for i in b_id:
        bookingid = i["bookingid"]
        url = f"{context.base_url}/booking/{bookingid}"
        context.response = APIRequest.get(url)
        assert context.response.status_code == 200, \
            f"Failed to get details for {bookingid}"


@then('the response status code should be 200')
def step_validate_status_code(context):
    assert context.response.status_code == 200, \
        f"Expected 200 but got {context.response.status_code}"


@then('the response should be valid')
def step_validate_response(context):
    response = context.response
    assert_status_code(response, 200)
    assert_header_present(response, "Content-Type")
    assert_key_in_response(response, ["id", "email"])
    assert_schema(response.json, "schemas/user_schema.json")
