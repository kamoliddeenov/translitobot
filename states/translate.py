from aiogram.dispatcher.filters.state import State, StatesGroup


class TranslateState(StatesGroup):
    message = State()
    send = State()
