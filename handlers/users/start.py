from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.misc.msg_dict import texts
from keyboards.inline.startKeyboard import menuStart
from loader import dp, db, bot
import asyncpg
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    try:
        if user[3] == message.from_user.id:
            if user[4] == "uzbek":
                await message.answer(texts["uz_start"])
            else:
                await message.answer(texts["en_start"])
    except:
        await message.answer(texts["choose_lang"], reply_markup=menuStart)


@dp.callback_query_handler(text="uzbek")
async def Salom(call: types.CallbackQuery):
    try:
        user = await db.add_user(telegram_id=call.from_user.id,
                                 full_name=call.from_user.full_name,
                                 username=call.from_user.username,
                                 lang="uzbek",
                                 sourc="auto",
                                 target="uz")
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=call.from_user.id)
    await call.message.delete()
    await call.message.answer(texts["uz_start"])


@dp.callback_query_handler(text="english")
async def Hello(call: types.CallbackQuery):
    try:
        user = await db.add_user(telegram_id=call.from_user.id,
                                 full_name=call.from_user.full_name,
                                 username=call.from_user.username,
                                 lang="english",
                                 sourc="auto",
                                 target="en")
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=call.from_user.id)
    await call.message.delete()
    await call.message.answer(texts["en_start"])


@dp.message_handler(text="/lang")
async def change_lang(msg: types.Message, state: FSMContext):
    await msg.answer(texts["choose_lang"], reply_markup=menuStart)
    await state.set_state("lang")


@dp.callback_query_handler(state='lang')
async def choose_lang(call: types.CallbackQuery, state: FSMContext):
    lang = call.data
    await db.update_user_lang(lang=lang, telegram_id=call.from_user.id)
    await call.message.delete()
    if lang == "uzbek":
        await call.message.answer(texts["set_uz"])
    elif lang == "english":
        await call.message.answer(texts["set_en"])
    await state.finish()


@dp.message_handler(state="lang")
async def post_unknown(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    if user[4] == "english":
        await message.answer("<b>Please choose your language.</>")
    else:
        await message.answer("<b>Iltimos tilni tanlang.</>")



