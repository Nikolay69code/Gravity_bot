import asyncio
import logging
from enum import IntEnum, auto
import random
from aiogram.filters.callback_data import CallbackData
from random import randint
import text_message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from config import TOKEN
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ShopActions(IntEnum):
    products = auto()
    address = auto()
    mylo = auto()
    wear = auto()
    root = auto()
    mass = auto()


class ShopCbData(CallbackData, prefix="shop"):
    action: ShopActions


class ProductActions(IntEnum):
    details = auto()
    update = auto()
    delete = auto()


class ProductCbData(CallbackData, prefix="product"):
    action: ProductActions
    id: int
    title: str
    price: int

def roli() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Я участник СВО",
        callback_data="solder",
    )
    builder.button(
        text="Я волонтер",
        callback_data="volonter",
    )
    builder.adjust(1)
    return builder.as_markup()

def build_shop_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Квадрокоптеры",
        callback_data=ShopCbData(action=ShopActions.products).pack(),
    )
    builder.button(
        text="Медицинская средства",
        callback_data=ShopCbData(action=ShopActions.address).pack(),
    )
    builder.button(
        text="Одежда и белье",
        callback_data=ShopCbData(action=ShopActions.wear).pack(),
    )
    builder.button(
        text="Личная гигиена",
        callback_data=ShopCbData(action=ShopActions.mylo).pack(),
    )
    builder.button(
        text="СПИСОК ВЫБРАННЫХ ТОВАРОВ",
        callback_data=ShopCbData(action=ShopActions.mass).pack(),
    )
    builder.adjust(2,2,1)
    return builder.as_markup()

def correct():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Все верно,подтверждаю👍",
        callback_data="yes",
    )
    builder.button(
        text="Нет,я не закончил❌",
        callback_data="no",
    )
    return builder.as_markup()
def build_products_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="⬅️НАЗАД",
        callback_data=ShopCbData(action=ShopActions.root).pack(),
    )
    for idx, (name, price) in enumerate(
        [
            ("Tablet", 999),
            ("Laptop", 1299),
            ("Desktop", 2499),
        ],
        start=1,
    ):
        builder.button(
            text=name,
            callback_data=ProductCbData(
                action=ProductActions.details,
                id=idx,
                title=name,
                price=price,
            ),
        )
    builder.adjust(1)
    return builder.as_markup()


def product_details_kb(
    product_cb_data: ProductCbData,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="⬅️НАЗАД",
        callback_data=ShopCbData(action=ShopActions.products).pack(),
    )
    for label, action in [
        ("Добавить", ProductActions.update),
        ("Удалить", ProductActions.delete),
    ]:
        builder.button(
            text=label,
            callback_data=ProductCbData(
                action=action,
                **product_cb_data.model_dump(include={"id", "title", "price"}),
                # **product_cb_data.model_dump(exclude={"action"}),
                # id=product_cb_data.id,
                # title=product_cb_data.title,
                # price=product_cb_data.price,
            ),
        )
    builder.adjust(1, 2)
    return builder.as_markup()


# def build_update_product_kb(
#     product_cb_data: ProductCbData,
# ) -> InlineKeyboardMarkup:
#     builder = InlineKeyboardBuilder()
#
#     builder.button(
#         text=f"⬅️ back to {product_cb_data.title}",
#         callback_data=ProductCbData(
#             action=ProductActions.details,
#             **product_cb_data.model_dump(include={"id", "title", "price"}),
#         ),
#     )
#     builder.button(
#         text="🔄 Update",
#         callback_data="...",
#     )
#     return builder.as_markup()









# class CategoryActions(IntEnum):
#     product = auto()
#     address = auto()
#     root = auto()
# class DIce_Model(CallbackData,prefix = "dice_model"):
#     act:CategoryActions
# class FixCbData(CallbackData,prefix = "fix-num"):
#     num:int
#
#
# class ProductActions(IntEnum):
#     details = auto()
#     update = auto()
#     delete = auto()
# class ProductCbData(CallbackData,prefix = "product"):
#     action:ProductActions
#     id : int
#     title:str
#     price:int
#
# def shoop_act():
#     builder = InlineKeyboardBuilder()
#     builder.adjust(1)
#     builder.button(text="Shop action", callback_data=DIce_Model(act=CategoryActions.product).pack())
#     builder.button(text="My address", callback_data=DIce_Model(act=CategoryActions.address).pack())
#     return builder.as_markup()
# def category_inline_keyboard(num = 0) -> InlineKeyboardMarkup:
#     builder = InlineKeyboardBuilder()
#     num = random.randint(0,100)
#     builder.button(text=f"{text_message.FOOD}", callback_data=text_message.FOOD_DATA)
#     builder.button(text=text_message.MEDICAL, callback_data=text_message.MEDICAL_DATA)
#     builder.button(text=text_message.DRONES, callback_data=text_message.DRONES_DATA)
#     builder.button(text=text_message.PROTECTION, callback_data=text_message.PROTECTION_DATA)
#     builder.adjust(1)
#     return builder.as_markup()
# def build_actions(random_number = "Random number"):
#     builder = InlineKeyboardBuilder()
#     builder.button(text=f"Back to root", callback_data=DIce_Model(act = CategoryActions.root).pack())
#     for idx,name,price in enumerate([("Tablet",1299),("Laptop",3209),("Desktop",2499)],start=1):
#         builder.button(text = name,callback_data=ProductCbData(action = ProductActions.details ,id=idx,title = name,price = price))
#     builder.adjust(1)
#     return builder.as_markup()