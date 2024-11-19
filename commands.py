import asyncio
import logging
import string

import inl_key_board
import text_message
import key_board
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart,Command
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router(name = __name__)


@router.message(Command("help"))
async def help_handler(message:Message):
    await message.answer(text = text_message.HELP, parse_mode=ParseMode.MARKDOWN_V2)

@router.message()
async def photo_handler(message:Message):
    await message.answer(text = "К сожалению мы не можем распознать ваше сообщение🤷‍♂️\n\n*Советуем пользоваться только кнопками🤗*",parse_mode=ParseMode.MARKDOWN_V2)
