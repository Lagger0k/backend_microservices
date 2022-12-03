from os import getenv
from dotenv import load_dotenv

load_dotenv()
RABBIT_HOST = getenv("RABBIT_HOST")
RABBIT_PORT = getenv("RABBIT_PORT")
WEB_SERVER_HOST = getenv("WEB_SERVER_HOST")
WEB_SERVER_PORT = getenv("WEB_SERVER_PORT")
