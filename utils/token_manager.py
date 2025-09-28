import requests
import os
from dotenv import load_dotenv
from config import BASE_URL

load_dotenv()


def get_token():
    url = f"{os.getenv('BASE_URL')}"
    payload = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }

    print("Token request to:", url)
    print("Payload:", payload)

    response = requests.post(url, json=payload)
    response.raise_for_status()

    token = response.json().get("token")
    print("Token received:", token)

    return token
