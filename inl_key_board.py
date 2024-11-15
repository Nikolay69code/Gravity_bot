import asyncio
import logging
import text_message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def category_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    buttons1 = [
        InlineKeyboardButton(text=text_message.MEDICAL, callback_data=text_message.MEDICAL_DATA)
    ]
    buttons2 = [InlineKeyboardButton(text=text_message.FOOD, callback_data=text_message.FOOD_DATA)]
    button3 = [InlineKeyboardButton(text=text_message.PROTECTION, callback_data=text_message.PROTECTION_DATA)]
    button4 = [InlineKeyboardButton(text=text_message.DRONES, callback_data=text_message.DRONES_DATA)]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons1,buttons2,button3,button4])
    builder.button(text=text_message.FOOD, callback_data=text_message.FOOD_DATA)
    builder.button(text=text_message.MEDICAL, callback_data=text_message.MEDICAL_DATA)
    
    return builder.as_markup()