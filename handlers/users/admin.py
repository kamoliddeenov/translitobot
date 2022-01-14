import asyncio

from keyboards.inline.admin import adminMenu, confirm_button
from aiogram import types
from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, db, bot
from states.admin import SendEveryOne

@dp.message_handler(Command("admin", prefixes=".!/"), user_id=ADMINS)
async def adminPanel(msg: types.Message):
    await msg.answer("<b>Boshqaruv paneliga xush kelibsiz.</>", reply_markup=adminMenu)


@dp.callback_query_handler(text="send", user_id=ADMINS)
async def sendAds(call: types.CallbackQuery):
    await call.message.reply("Foydalanuvchilarga yubormoqchi bo'lgan reklama postingizni yuboring.")
    await SendEveryOne.post.set()


@dp.message_handler(state=SendEveryOne.post)
async def admin(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text)
    await message.answer("Post barcha foydalanuvchilarga yuborilsinmi?",
                         reply_markup=confirm_button)
    await SendEveryOne.next()


@dp.callback_query_handler(text="post", state=SendEveryOne.ask_send)
async def confirm_post(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Yuborildi")
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        # print(user[4])
        try:
            await bot.send_message(chat_id=user_id, text=text)
        except:
            pass
        await asyncio.sleep(0.05)


@dp.callback_query_handler(text="stat", user_id=ADMINS)
async def Stat(call: types.CallbackQuery):
    count = await db.count_users()
    await call.message.answer(text=f"Bazada {count} ta foydalanuvchi bor.")
