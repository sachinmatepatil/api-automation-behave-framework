import requests
from utils.logger import get_logger

logger = get_logger()


class APIRequest:
    @staticmethod
    def get(url, headers=None):
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url, headers=headers)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response

    @staticmethod
    def post(url, data=None, headers=None):
        logger.info(f"Sending POST request to {url} with payload: {data}")
        response = requests.post(url, json=data, headers=headers)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response

    @staticmethod
    def put(url, data=None, headers=None):
        logger.info(f"Sending PUT request to {url}")
        response = requests.put(url, json=data, headers=headers)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response

    @staticmethod
    def delete(url, headers=None):
        logger.info(f"Sending DELETE request to {url}")
        response = requests.delete(url, headers=headers)
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        return response
