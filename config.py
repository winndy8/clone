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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAhLEVj0zT3nbeQ_DrQf44p0FpFwJBP4rh3WRneIOTNqv_oA7rU7YE3aT5xFX8-RmKqalRvb36EEoHndyQgZOnaP9q1_wfsIeCbyZuE3KDMnA63Tmog6DJJ-Fd_AxC7Xj2vZm3R1iud61amWlizzYbWWO0r5TqFB9IXiX9gmNiFyCqVTN81T6AEYL-dCK0DOTiKSbb22rbRGJYUeLQCEBAdd7pv3bJK0RIRPq4EZdUud9RPpCf4U_6QTahmSWETCFWU_uRFTQ0FWz1o5o-3y5qJuyqNM8Ixwoq8tEXgazbx-j6nvE3xiW_0FoVe5FxtE1CMEJduY3VR_0oZ577NeByEAAAAATy6BAcA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://clone:clone@cluster0.go11yez.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
