import asyncio
import logging

import config
import key_board
import text_message
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from handlers import router
from inl_key_board import roli

bot = Bot(token =  TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def send_message_by_username(username: str, text: str):
    try:
        chat = await bot.get_chat(username)
        if chat is not None:
            await bot.send_message(chat.id, text)
            print(f"Сообщение отправлено пользователю с username '@{username}'")
        else:
            print(f"Пользователь с username '@{username}' не найден")
    except Exception as e:
        print(f"Произошла ошибка при отправке сообщения: {e}")
@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(text = text_message.WELCOME, parse_mode=ParseMode.MARKDOWN_V2,reply_markup=roli())
# Пример использования функции
@dp.message(Command("send"))
async def sent(message:Message):
    username = config.ADMIN_USERNAME  # Замените example_user на нужный вам username
    text = "Пример сообщения!"
    await send_message_by_username(username, text)
    await message.answer(text = "Сообщение отправлено")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
#if "__name__" == "__main__":
asyncio.run(main())