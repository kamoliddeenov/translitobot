from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menusrc = InlineKeyboardMarkup(row_width=2)

langs = {
    "🇬🇧 English": "en",
    "🇺🇿 Uzbek": "uz",
    "🇷🇺 Russian": "ru",
    "🇰🇷 Korean": "ko",
    "🇸🇦 Arabic": "ar",
    "🇹🇷 Turkish": "tr",
    "🇨🇳 Chinese": "zh-TW",
    "🇯🇵 Japanse": "ja",
    "🇮🇩 Indonesian": "id",
    "🇰🇿 Kazakh": "kk",
    "🇰🇬 Kyrgyz": "ky",
    "🇮🇷 Persian": "fa",
    "🇮🇹 Italian": "it",
    "🇪🇸 Spanish": "es"
}

for text, data in langs.items():
    menusrc.insert(InlineKeyboardButton(text=text, callback_data=data))
menusrc.add(
    InlineKeyboardButton(text="🅰️ Auto Detect", callback_data="auto")
)

menutarget = InlineKeyboardMarkup(row_width=2)
langstarget = {
    "🇬🇧 English": "en",
    "🇺🇿 Uzbek": "uz",
    "🇷🇺 Russian": "ru",
    "🇰🇷 Korean": "ko",
    "🇸🇦 Arabic": "ar",
    "🇹🇷 Turkish": "tr",
    "🇨🇳 Chinese": "zh-TW",
    "🇯🇵 Japanse": "ja",
    "🇮🇩 Indonesian": "id",
    "🇰🇿 Kazakh": "kk",
    "🇰🇬 Kyrgyz": "ky",
    "🇮🇷 Persian": "fa",
    "🇮🇹 Italian": "it",
    "🇪🇸 Spanish": "es"
}

for text, data in langstarget.items():
    menutarget.insert(InlineKeyboardButton(text=text, callback_data=data))
