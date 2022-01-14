from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Restart bot"),
            types.BotCommand("translate", "Choose language for translations"),
            types.BotCommand("lang", "Choose your language"),
            types.BotCommand("help", "Yordam"),
        ]
    )
