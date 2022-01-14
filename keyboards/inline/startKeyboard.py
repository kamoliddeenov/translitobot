from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menuStart = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="uzbek"),
        InlineKeyboardButton(text="🇬🇧 English", callback_data="english"),
    ]]
)
