import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SECRET_PHRASE = os.getenv("SECRET_PHRASE", "МЯУ")
