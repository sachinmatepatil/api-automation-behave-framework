from utils.testdata_loader import load_test_data
from utils.request_helper import APIRequest
from config import BASE_URL
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

@when('I send a POST request to "/booking" using dataset "{index}"')
def step_send_post_request_dataset(context, index):
    index = int(index)

    # Load JSON test data
    test_data = load_test_data("booking_data.json")[index]

    payload = {
        "firstname": test_data["firstname"],
        "lastname": test_data["lastname"],
        "totalprice": test_data["totalprice"],
        "depositpaid": test_data["depositpaid"],
        "bookingdates": {
            "checkin": test_data["checkin"],
            "checkout": test_data["checkout"]
        },
        "additionalneeds": test_data["additionalneeds"]
    }

    url = f"{context.base_url}/booking"
    context.response = APIRequest.post(url, json=payload)
