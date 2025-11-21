from dotenv import load_dotenv
import os

# Load environment variable from .env
load_dotenv()

# Default to the public Restful Booker API if no BASE_URL is provided
BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
