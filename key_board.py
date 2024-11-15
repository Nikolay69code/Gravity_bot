import asyncio
import logging
import text_message

from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def start_keyboard():
     buttons_row = [KeyboardButton(text=text_message.SOlDERS_BUTTON),
                    KeyboardButton(text=text_message.VOLUNTEER_BUTTON)]
     keyb = ReplyKeyboardMarkup(keyboard=[buttons_row],resize_keyboard=True)
     return keyb
def kategory_keyboard():
    buttons_row = [KeyboardButton(text=text_message.CATEGORY),
                   KeyboardButton(text=text_message.DELETE)]
    keyb = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
    return keyb
