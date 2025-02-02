from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="check_imei"))
    builder.add(KeyboardButton(text="check_balance"))
    builder.add(KeyboardButton(text="check_services"))
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)
