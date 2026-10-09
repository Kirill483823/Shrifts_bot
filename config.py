import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
FILE_ID_IMAGE = os.getenv("FILE_ID_IMAGE")
FILE_ID_FOR_WAITING_TEXT = os.getenv("FILE_ID_FOR_WAITING_TEXT")

if not BOT_TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден в файле .env")
