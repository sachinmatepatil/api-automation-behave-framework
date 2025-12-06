from utils.token_manager import get_token
from config import BASE_URL
from dotenv import load_dotenv


def before_all(context):
    load_dotenv()
    context.base_url = BASE_URL
    context.token = get_token()
