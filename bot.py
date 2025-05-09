import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from setting import BOT_TOKEN, SECRET_PHRASE
import db

logging.basicConfig(level=logging.INFO, filename="botLogs.log",filemode="w",format="%(asctime)s %(levelname)s %(message)s")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_all_messages(message: types.Message):
    text = message.text.strip()

    if text == "/start":
        db.add_user(message.from_user.id)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Получить Ключ", callback_data="get_vpn")]
        ])

        await message.answer("Добро пожаловать!", reply_markup=keyboard)
        
    elif text == SECRET_PHRASE:
        db.allow_user(message.from_user.id)
        await message.answer("✅ Вам выдан доступ!")
    else:
        pass


@dp.callback_query()
async def handle_buttons(callback: types.CallbackQuery):
    if callback.data == "get_vpn":
        await callback.message.answer("В разработке")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.info("Bot started")
    asyncio.run(main())