from behave import given, when, then
from utils.token_manager import get_token


@given("I generate a valid token")
def step_impl(context):
    context.token = get_token()
    assert context.token is not None
    print("Token generated:", context.token)


