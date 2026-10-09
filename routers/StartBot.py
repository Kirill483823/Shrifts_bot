from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from keyboards.keyboard_for_main_menu import main_menu_keyboard, go_back_to_main_menu
from config import FILE_ID_IMAGE
from States.bot_states import States_bot

start_router = Router()

"""Блок отвечает за главное меню"""

"""Функция отправляющая главное меню"""
async def send_start_menu(message: Message | None, callback: CallbackQuery | None, state: FSMContext):
    text = "❇️ Привет, отправь текст для того чтобы я сделал его в красивом стиле."
    photo = FILE_ID_IMAGE

    await state.clear()
    await state.set_state(States_bot.be_in_main_menu)

    if message:
        await message.answer_photo(photo=photo, caption=text,\
                                    reply_markup=main_menu_keyboard())
    else:
        await callback.message.answer_photo(photo=photo, caption=text,\
                                            reply_markup=main_menu_keyboard())


"""Реакция на комманду /start"""
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await send_start_menu(message, None, state)


"""Реакция на кнопку на главную"""
@start_router.callback_query(F.data=="back_button_to_main_menu")
async def back_click_to_main(callback: CallbackQuery, state: FSMContext):
    await callback.answer("✅Возвращаемся на главную")

    if callback.message:
        try:
            await callback.message.delete()# удаление сообщения под которым была
        except Exception:                  # нажата кнопка "На главную" с проверкой
            pass                           # на существование этого сообщения

    await send_start_menu(None, callback, state)

"""обработка главного меню"""
@start_router.callback_query(F.data == "info")
async def click_to_info(callback: CallbackQuery):
    await callback.answer("❔Инфо")

    try:
        await callback.message.delete()
    except Exception:
        pass

    text = "🔩 Бот находится в разработке, так что если найдёте ошибку или баг, пишите: @CubikCode"

    await callback.message.answer(text, reply_markup=go_back_to_main_menu())