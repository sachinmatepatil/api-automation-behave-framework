import json
from behave import given, when, then
from config import BASE_URL
from utils.request_helper import APIRequest


@given('the API base URL is set')
def step_set_base_url(context):
    context.base_url = BASE_URL


@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.response = APIRequest.get(url)


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


