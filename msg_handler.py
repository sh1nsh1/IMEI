import itertools
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove
from FSMStates import States
from middleware import validate_imei
from keyboards import menu_kb
import api

r = Router()


@r.message(CommandStart())
async def start(msg: types.Message, state: FSMContext):
    await msg.answer("Hello, please provide your token")
    await state.set_state(States.ask_token)


@r.message(States.ask_token)
async def check_token(msg: types.Message, state: FSMContext):
    if await api.check_token(msg.text):
        await msg.answer(
            "Token is valid, Welcome. Here's what you can do", reply_markup=menu_kb()
        )
        await state.set_state(States.authed)
        # TODO add to the whitelist
        await state.update_data({"token": msg.text})


@r.message(States.authed and (F.text == "check_imei"))
async def ask_imei(msg: types.Message, state: FSMContext):
    await msg.answer(
        "Please provide your IMEI you want to check", reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(States.ask_imei)


@r.message(States.ask_imei)
async def check_imei(msg: types.Message, state: FSMContext):
    imei = msg.text
    data = await state.get_data()
    await msg.answer("Pending...")

    if await validate_imei(imei):
        result = await api.check_imei(imei, data["token"])

        for result_batch in itertools.batched(result, 4096):
            text = "".join(result_batch)
    else:
        text = "Your IMEI is not valid"

    await state.set_state(States.authed)

    await msg.answer(text, reply_markup=menu_kb())


@r.message(States.authed and (F.text == "check_balance"))
async def check_balance(msg: types.Message, state: FSMContext):
    data = await state.get_data()

    await msg.answer("Pending...")

    balance = await api.get_balance(data["token"])
    text = f"Yout balance is {balance}$"

    await msg.answer(text, reply_markup=menu_kb())


@r.message(States.authed and (F.text == "check_services"))
async def check_services(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    await msg.answer("Pending...")

    services = await api.get_services(data["token"])
    await msg.answer("Here's out serivices")
    await msg.answer(services)
