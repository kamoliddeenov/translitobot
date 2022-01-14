from aiogram import types
from deep_translator import GoogleTranslator, single_detection

from keyboards.default.backmenu import menuback
from keyboards.inline.languages import menutarget, menusrc
from loader import dp, db


@dp.message_handler(state=None)
async def Translate(message: types.Message):
    text = message.text
    lang = await db.select_user(telegram_id=message.from_user.id)
    try:
        translated = GoogleTranslator(source=lang[5], target=lang[6]).translate(text=text)
        await message.answer(text=f"{lang[5]} - {lang[6]}\n\n{translated}")
    except:
        await message.answer(text=message.text)
