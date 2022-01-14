from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db
from utils.misc.msg_dict import texts


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    lang = await db.select_user(telegram_id=message.from_user.id)
    if lang[4] == "uzbek":
        await message.answer(texts["help_uz"])
    elif lang[4] == "english":
        await message.answer(texts["help_en"])
