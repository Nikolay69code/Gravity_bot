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
from commands import router as commands_router
router = Router(name = __name__)
router.include_router(commands_router)
@router.callback_query(F.data == text_message.DRONES_DATA)
async def drones_query(callback_query:CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(text = f"Вы выбрали категорию {text_message.DRONES}")

@router.callback_query(F.data == text_message.MEDICAL_DATA)
async def drones_query(callback_query:CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(text = f"Вы выбрали категорию '{text_message.MEDICAL}'")
    await callback_query.message.answer(text = "Четвертой кнопки все еще нет")

@router.callback_query(F.data == text_message.PROTECTION_DATA)
async def drones_query(callback_query:CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(text = f"Вы выбрали категорию '{text_message.PROTECTION}'")

@router.callback_query(F.data == text_message.FOOD_DATA)
async def drones_query(callback_query: CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(text=f"Вы выбрали категорию '{text_message.FOOD}'")