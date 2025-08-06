from dotenv import load_dotenv
import os

# Load environment variable from .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
