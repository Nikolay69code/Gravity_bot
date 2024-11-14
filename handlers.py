import asyncio
import logging
import text_message
import key_board
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
router = Router()

@router.message(CommandStart())
async def start_hendler(message:Message):
    await message.answer(text = text_message.WELCOME, parse_mode=ParseMode.MARKDOWN_V2,reply_markup=key_board.start_keyboard())


@router.message(Command("help"))
async def help_handler(message:Message):
    await message.answer(text = text_message.HELP, parse_mode=ParseMode.MARKDOWN_V2)

@router.message(F.text == text_message.SOlDERS_BUTTON)
async def help_handler(message:Message):
    await message.answer(text = text_message.SOlDERS_DESCRIPTION, parse_mode=ParseMode.MARKDOWN_V2,reply_markup = key_board.kategory_keyboard())
    keyb = key_board.category_inline_keyboard()
    await message.answer("Выберите одну из категорий.", reply_markup=keyb)

@router.message(F.text == text_message.VOLUNTEER_BUTTON)
async def help_handler(message:Message):
    await message.answer(text = text_message.VOLUNTEER_DESCRIPTION, parse_mode=ParseMode.MARKDOWN_V2,reply_markup = key_board.kategory_keyboard())
    keyb = key_board.category_inline_keyboard()
    await message.answer("Выберите одну из категорий.", reply_markup=keyb)
# @dp.message(F.photo)
# async def photo_handler(message:Message):
#     await message.answer(text = "К сожалению мы не распознаем фото🤷‍♂️")
# @dp.message(F.video)
# async def photo_handler(message:Message):
#     await message.answer(text = "К сожалению мы не распознаем видео🤷‍♂️")
# @dp.message(F.document)
# async def photo_handler(message:Message):
#     await message.answer(text = "К сожалению мы не распознаем документы🤷‍♂️")
# @dp.message(F.stikers)
# async def photo_handler(message:Message):
#     await message.answer(text = "К сожалению мы не распознаем стикеры🤷‍♂️")
# @dp.message(F.emoji)
# async def photo_handler(message:Message):
#     await message.answer(text = "К сожалению мы не распознаем эмодзи🤷‍♂️")
# @dp.message(F.gifs)
# async def photo_handler(message:Message):
#     await message.answer(text = "К сожалению мы не распознаем гифки🤷‍♂️")
@router.message(Command(text_message.PROTECTION))
async def help_handler(message:Message):
    await message.answer(text = text_message.SOlDERS_DESCRIPTION, parse_mode=ParseMode.MARKDOWN_V2)

@router.message(Command(text_message.MEDICAL))
async def help_handler(message:Message):
    await message.answer(text = text_message.SOlDERS_DESCRIPTION, parse_mode=ParseMode.MARKDOWN_V2)

@router.message(Command(text_message.DRONES))
async def help_handler(message:Message):
    await message.answer(text = text_message.SOlDERS_DESCRIPTION, parse_mode=ParseMode.MARKDOWN_V2)

@router.message(Command("Свои варианты"))
async def help_handler(message:Message):
    await message.answer(text = "Введите свои варианты")

@router.message()
async def photo_handler(message:Message):
    await message.answer(text = "К сожалению мы не можем распознать ваше сообщение🤷‍♂️\n\n*Советуем пользоваться только кнопками🤗*",parse_mode=ParseMode.MARKDOWN_V2)
