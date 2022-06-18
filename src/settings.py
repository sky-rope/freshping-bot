import logging
from environs import Env

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S")

env = Env()
LISTEN_PORT = env.int("LISTEN_PORT", default=9088)
LISTEN_HOST = env.str("LISTEN_HOST", default="0.0.0.0")
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN", default="YOUR_BOT_TOKEN")
TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID", default="TELEGRAM_CHAT_ID")
