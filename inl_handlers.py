import asyncio
import logging
import string
import text_message
import key_board
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message, CallbackQuery, callback_query
from aiogram.filters import CommandStart, Command, callback_data
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from commands import router as commands_router
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown


router = Router(name = __name__)
router.include_router(commands_router)

from inl_key_board import (
    ShopCbData,
    ShopActions,
    build_shop_kb,
    build_products_kb,
    ProductCbData,
    ProductActions,
    product_details_kb, correct,
)

@router.callback_query(
    ShopCbData.filter(F.action == ShopActions.products),
)
async def send_products_list(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Список различных моделей FPV дронов и квадрокоптеров:",
        reply_markup=build_products_kb(),
    )

@router.callback_query(
    ShopCbData.filter(F.action == ShopActions.wear),
)
async def send_wear_list(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Виды бронезащиты,одежды и белья",
        reply_markup=build_products_kb(),
    )

@router.callback_query(
    ShopCbData.filter(F.action == ShopActions.mylo),
)
async def send_wear_list(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Список требуемых средств личной гигиены:",
        reply_markup=build_products_kb(),
    )


@router.callback_query(
    ShopCbData.filter(F.action == ShopActions.mass),
)
async def send_wear_list(call: CallbackQuery):
    await call.message.answer(
        text="Это список выбранных вами позици, все верно?\n\n\n",
        reply_markup=correct()
    )

@router.callback_query(
    ShopCbData.filter(F.action == ShopActions.root),
)
async def handle_my_address_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Выберите необходимые товары из предоставленных категорий",
        reply_markup=build_shop_kb(),
    )
@router.callback_query(
    ShopCbData.filter(F.action == ShopActions.address),
)
async def handle_my_address_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Список требуемого медицинского оснащения:",
        reply_markup=build_products_kb(),
    )

@router.callback_query(
    ProductCbData.filter(F.action == ProductActions.details),
)
async def handle_product_details_button(
    call: CallbackQuery,
    callback_data: ProductCbData,
):
    await call.answer()
    message_text = markdown.text(
        markdown.hbold(f"Product №{callback_data.id}"),
        markdown.text(
            markdown.hbold("Title:"),
            callback_data.title,
        ),
        markdown.text(
            markdown.hbold("Price:"),
            callback_data.price,
        ),
        sep="\n",
    )
    await call.message.edit_text(
        text=message_text,
        reply_markup=product_details_kb(callback_data),
    )


@router.callback_query(
    ProductCbData.filter(F.action == ProductActions.update),
)
async def handle_product_update_button(
    call: CallbackQuery,
    callback_data: ProductCbData,
):
    await call.answer("Продукт успешно добавлен в список")

@router.callback_query(
    ProductCbData.filter(F.action == ProductActions.delete),
)
async def handle_product_delete_button(
    call: CallbackQuery,
):
    await call.answer(
        text="Продукт успешно удален из списка",
    )

@router.callback_query(F.data == "solder")
async def solder(call: CallbackQuery):
    await call.message.answer(text = "Хорошо, выберите категорию, а затем остро необходимые вам товары на данный момент:",reply_markup=build_shop_kb())
@router.callback_query(F.data == "volonter")
async def solder(call: CallbackQuery):
    await call.message.answer(text = "Отлично, выберите категорию вещей, а затем товары, которые вы готовы приобрести в пользу наших бойцов на передовой:",reply_markup=build_shop_kb())
    # num = 0
@router.callback_query(F.data == "yes")
async def solder(call: CallbackQuery):
    await call.message.answer(text = "Ваше заявление успешно отправлено👌! С вами свяжется администратор в случае метча")
@router.callback_query(F.data == "no")
async def solder(call: CallbackQuery):
    await call.message.answer(text = "Продолжайте выбирать",reply_markup=build_shop_kb())
# @router.callback_query(F.data == text_message.DRONES_DATA)
# async def drones_query(callback_query:CallbackQuery):
#     bot_me = await callback_query.bot.me()
#     await callback_query.message.answer(text = f"Вы выбрали категорию {text_message.DRONES}")
#
# @router.callback_query(F.data == text_message.MEDICAL_DATA)
# async def drones_query(callback_query:CallbackQuery):
#     bot_me = await callback_query.bot.me()
#     await callback_query.message.answer(text = f"Вы выбрали категорию '{text_message.MEDICAL}'")
# @router.callback_query(F.data == text_message.PROTECTION_DATA)
# async def drones_query(callback_query:CallbackQuery):
#     bot_me = await callback_query.bot.me()
#     await callback_query.message.answer(text = f"Вы выбрали категорию '{text_message.PROTECTION}'")
#
# @router.callback_query(F.data == text_message.FOOD_DATA)
# async def drones_query(callback_query: CallbackQuery):
#     await callback_query.message.answer(text=f"Вы выбрали категорию '{text_message.FOOD}'")
# @router.callback_query(DIce_Model.filter(F.act == CategoryActions.product))
# async def handle_target_food(callback_query:CallbackQuery):
#     await callback_query.answer(text=f"Product in progress")
# @router.callback_query(DIce_Model.filter(F.act == CategoryActions.root))
# async def handle_target_food(callback_query:CallbackQuery):
#     await callback_query.message.answer(text=f"И снова мы на главной странице",reply_marcup = key_board.start_keyboard())
#
# @router.callback_query(DIce_Model.filter(F.act == CategoryActions.address))
# async def handle_target_food(callback_query:CallbackQuery):
#     await callback_query.answer(text=f"Your address in progress")
#
# @router.callback_query(FixCbData.filter())
# async def handle_food(callback_query:CallbackQuery,callback_data:FixCbData):
#     await callback_query.answer(text=f"Твое рандомное значение равняется {callback_data.num}\n and {callback_query.data!r} ")