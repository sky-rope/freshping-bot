import logging
from aiogram import Bot, Dispatcher
from settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message()
async def send_message(text):
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
