from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


adminMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🙆🏻‍♂️ Barchaga xabar", callback_data="send"),
        ],
        [
            InlineKeyboardButton(text="📊 Statistika", callback_data="stat"),
        ]
    ]
)

confirm_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data="post"),
            InlineKeyboardButton(text="Yo'q", callback_data="cancel")
        ]
    ]
)