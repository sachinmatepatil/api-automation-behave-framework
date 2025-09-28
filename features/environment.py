from utils.token_manager import get_token
import os
from dotenv import load_dotenv


def before_all(context):
    load_dotenv()
    context.base_url = os.getenv("BASE_URL")
    context.token = get_token()
