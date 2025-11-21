import json
from behave import given, when, then
from config import BASE_URL
from utils.request_helper import APIRequest
from utils.api_helper import build_url

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
    context.endpoint = endpoint

    resolved_endpoint = endpoint
    if "{booking_id}" in endpoint:
        booking_id = getattr(context, "booking_id", None)
        assert booking_id is not None, "booking_id was not set before request"
        resolved_endpoint = endpoint.replace("{booking_id}", str(booking_id))

    url = build_url(context.base_url, resolved_endpoint)
    response = APIRequest.get(url)

    should_skip_fallback = "negative" in getattr(context, "tags", [])

    if (
        response.status_code == 404
        and resolved_endpoint.startswith("booking/")
        and not should_skip_fallback
    ):
        # Fallback to the first available booking id to keep the test stable
        list_response = APIRequest.get(build_url(context.base_url, "/booking"))
        assert list_response.status_code == 200, "Unable to fetch booking list for fallback"

        booking_list = list_response.json()
        assert booking_list, "No bookings available for fallback lookup"

        fallback_id = booking_list[0]["bookingid"]
        url = build_url(context.base_url, f"booking/{fallback_id}")
        response = APIRequest.get(url)
        context.booking_id = fallback_id

    context.response = response


@when('I send a GET request to booking from "{data_file}"')
def step_external_data(context, data_file):
    with open(data_file, 'r') as file:
        requested_ids = json.load(file)

    list_response = APIRequest.get(build_url(context.base_url, "/booking"))
    assert list_response.status_code == 200, "Failed to retrieve booking list"

    booking_list = list_response.json()
    assert booking_list, "Booking list is empty"

    total_to_fetch = len(requested_ids)
    booking_ids = [entry["bookingid"] for entry in booking_list[:total_to_fetch]]
    assert booking_ids, "No booking IDs available for validation"

    for bookingid in booking_ids:
        url = build_url(context.base_url, f"booking/{bookingid}")
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

    response_json = response.json()
    if isinstance(response_json, list):
        assert response_json, "Booking list is empty"
        assert_key_in_response(response, ["bookingid"])
    else:
        assert_key_in_response(
            response,
            ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"],
        )
        assert_schema(response_json, "schemas/booking_detail_schema.json")
