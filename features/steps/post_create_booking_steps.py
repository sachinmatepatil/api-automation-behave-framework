import json
from behave import given, when, then
from config import BASE_URL
from utils.request_helper import APIRequest
from utils.api_helper import post_with_retry
from utils.assertions import assert_schema
from utils.assertions import (
    assert_status_code,
    assert_schema,
    assert_header_present,
    assert_key_in_response
)


# @given('the API base URL is set')a
# def step_set_base_url(context):
#     context.base_url = BASE_URL


@when('I send a POST request to "{endpoint}" with the following details')
def step_send_post_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"

    # Parse the table data into a dictionary
    payload = {
        'firstname': context.table[0]['firstname'],
        'lastname': context.table[0]['lastname'],
        'totalprice': int(context.table[0]['totalprice']),
        'depositpaid': context.table[0]['depositpaid'].lower() == 'true',
        'bookingdates': {
            'checkin': context.table[0]['checkin'],
            'checkout': context.table[0]['checkout']
        },
        'additionalneeds': context.table[0]['additionalneeds']
    }

    # Send the POST request and store the response
    context.response = APIRequest.post(url, json=payload)


@then('the response should contain the booking id')
def step_validate_booking_id(context):
    response_json = context.response.json()
    assert 'bookingid' in response_json, "Response does not contain 'bookingid'"


@then('the firstname should be "{expected_firstname}"')
def step_validate_firstname(context, expected_firstname):
    response_json = context.response.json()
    actual_firstname = response_json.get('booking', {}).get('firstname')
    assert actual_firstname == expected_firstname, \
        f"Expected firstname '{expected_firstname}' but got '{actual_firstname}'"


@then('the lastname should be "{expected_lastname}"')
def step_validate_lastname(context, expected_lastname):
    response_json = context.response.json()
    actual_lastname = response_json.get('booking', {}).get('lastname')
    assert actual_lastname == expected_lastname, \
        f"Expected lastname '{expected_lastname}' but got '{actual_lastname}'"

@then('the response status code should be 400')
def step_validate_status_code_400(context):
    assert_status_code(context.response, 400)

@then('the response should contain an error message indicating invalid input')
def step_validate_error_message(context):
    response_json = context.response.json()
    assert_key_in_response(response_json, 'error')
    expected_error_message = "Invalid input"
    actual_error_message = response_json.get('error')
    assert actual_error_message == expected_error_message, \
        f"Expected error message '{expected_error_message}' but got '{actual_error_message}'"

@then("the response should match create booking schema")
def step_validate_create_booking_schema(context):
    assert_schema(context.resonse.json(), "create-booking-schema.json")
