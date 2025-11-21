import os
import requests
from dotenv import load_dotenv
from config import BASE_URL
from utils.api_helper import build_url

load_dotenv()


def get_token():
    """Request an auth token from Restful Booker using configured credentials."""
    url = build_url(os.getenv("BASE_URL", BASE_URL), "auth")
    username = os.getenv("USERNAME", "admin")
    password = os.getenv("PASSWORD", "password123")
    payload = {"username": username, "password": password}

    print("Token request to:", url)

    response = requests.post(url, json=payload)
    response.raise_for_status()

    token = response.json().get("token")
    if not token:
        raise ValueError("Auth token not found in response")

    return token
