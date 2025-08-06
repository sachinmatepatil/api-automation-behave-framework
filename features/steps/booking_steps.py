from behave import given, when, then
import requests
from config import BASE_URL
from utils.request_helper import APIRequest


@given('the API base URL is set')
def step_set_base_url(context):
    context.base_url = BASE_URL


@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    url = f"{context.base_url}{endpoint}"
    context.response = APIRequest.get(url)


@then('the response status code should be 200')
def step_validate_status_code(context):
    assert context.response.status_code == 200, \
        f"Expected 200 but got {context.response.status_code}"
