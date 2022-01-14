from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from deep_translator import GoogleTranslator, single_detection

from keyboards.default.backmenu import menuback
from keyboards.inline.languages import menusrc, menutarget
from loader import dp, db
from utils.misc.translate import Translator


@dp.message_handler(text="/translate")
async def chooseLang(message: Message):
    lang = await db.select_user(telegram_id=message.from_user.id)  # lang[4] = til
    if lang[4] == "uzbek":
        await message.answer("<b>Matn qaysi tilda:</>", reply_markup=menusrc)
    elif lang[4] == "english":
        await message.answer("<b>Select the source language:</>", reply_markup=menusrc)


@dp.callback_query_handler()
async def srcdetect(call: CallbackQuery, state: FSMContext):
    src = call.data
    await state.set_state("source")
    await db.update_source_lang(sourc=src, telegram_id=call.from_user.id)
    lang = await db.select_user(telegram_id=call.from_user.id)
    if lang[4] == "uzbek":
        await call.message.edit_text("<b>Qaysi tilga tarjima qilmoqchisiz:</>", reply_markup=menutarget)
    elif lang[4] == "english":
        await call.message.edit_text("<b>Which language do you want to translate:</>", reply_markup=menutarget)


@dp.callback_query_handler(state="source")
async def srctarget(call: CallbackQuery, state: FSMContext):
    target = call.data
    await state.finish()
    await db.update_target_lang(target=target, telegram_id=call.from_user.id)
    lang = await db.select_user(telegram_id=call.from_user.id)  # lang[4] = til
    if lang[4] == "uzbek":
        await call.message.edit_text("<b>Tarjima qilmoqchi bo'lgan matnni yuboring:</>")
    elif lang[4] == "english":
        await call.message.edit_text("<b>Enter the text to be translated:</>")


@dp.message_handler(state="source")
async def post_unknown(message: Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    if user[4] == "english":
        await message.answer("<b>Which language do you want to translate. Please select it.</>")
    else:
        await message.answer("<b>Qaysi tilga tarjima qilmoqchisiz. Iltimos tanlang.</>")