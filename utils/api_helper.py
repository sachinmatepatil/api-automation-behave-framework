import requests
import logging
from time import sleep
from urllib.parse import urljoin


def build_url(base_url: str, endpoint: str) -> str:
    """Join a base URL and endpoint ensuring exactly one slash between them."""
    if not base_url:
        raise ValueError("Base URL is not set")

    normalized_base = base_url.rstrip('/') + '/'
    normalized_endpoint = endpoint.lstrip('/')
    return urljoin(normalized_base, normalized_endpoint)


# Reusable GET request with retries and timeout
def get_with_retry(url, headers=None, retries=3, timeout=5):
    attempt = 0
    while attempt < retries:
        try:
            logging.info(f"GET Attempt {attempt + 1} to {url}")
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.warning(f"Request failed: {e}")
            attempt += 1
            sleep(1)  # Wait before retrying
    raise Exception(f"Failed to GET {url} after {retries} attempts")


# Reusable POST request with retries and timeout
def post_with_retry(url, data=None, headers=None, retries=3, timeout=5):
    attempt = 0
    while attempt < retries:
        try:
            logging.info(f"POST Attempt {attempt + 1} to {url} with data: {data}")
            response = requests.post(url, json=data, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.warning(f"Request failed: {e}")
            attempt += 1
            sleep(1)
    raise Exception(f"Failed to POST {url} after {retries} attempts")
