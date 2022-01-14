from aiogram.dispatcher.filters.state import State, StatesGroup


class SendEveryOne(StatesGroup):
    post = State()
    ask_send = State()
