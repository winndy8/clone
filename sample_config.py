#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6153177382:AAFHSghOCWr-wEQOBpE_1T7Bu91-sAthPGY")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "2790569"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "7c72307ff7c7e44d2b416e551145f5ba")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQB7iIRYmGsUgoQdl6EuYCFkIPnAp1K7Bch9LrRC6T-IyuvU-5RIfOwxbitxtAzvZIf6H2fgnDPKFJp3nhUYti2F3S9ZEK7KyLMlfvSVCvEP81on8end0Z_xDJXKbFVncpypuWLrr8vg9hBSVfdccAfpl9Yf3YYnxG_S21w1Kx1E1iDa8nexpxVil2hX4Nria4vmNd3gVDau85MIzYKfN3nEjfhk9NMlgncMhJyZNmWoNA0huV6UDrYGHrkO8h3aOHkxbCfg5TkN3rzt7S6HIe4jp9ZVKAd2evSP1mduINtPKgHScvO5rpE7axbPRgLheQdn7Hg9MlRSgfHRgLS26dxxAAAAATy6BAcA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://clone:clone@cluster0.go11yez.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
