import os
from telegram.bot import Bot

def notify_telegram(key: str, chatid: int, text: str):
    bot = Bot(key)
    bot.send_message(chat_id=chatid, text=f"[{os.path.basename(os.getcwd())}]\n{text}")