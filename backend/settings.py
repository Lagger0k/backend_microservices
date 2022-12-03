from os import getenv
from dotenv import load_dotenv

load_dotenv()
RABBIT_HOST = getenv('RABBIT_HOST')
RABBIT_PORT = getenv('RABBIT_PORT')
