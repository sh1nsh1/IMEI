from aiogram.fsm.state import State,StatesGroup


class States(StatesGroup):
    ask_token = State()
    authed = State()
    ask_imei = State()
