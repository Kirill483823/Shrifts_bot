from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from keyboards.keyboard_for_main_menu import main_menu_keyboard, go_back_to_main_menu
from config import FILE_ID_IMAGE
from States.bot_states import States_bot

start_router = Router()

"""Блок отвечает за главное меню и инфо"""

#Функция отправляющая главное меню
async def send_start_menu(message: Message | None, callback: CallbackQuery | None, state: FSMContext):
    text = "❇️ Привет! Я помогу тебе офрмить твой текст красивым шрифтом.\n\n"\
        "⚠️ Можно использовать любые буквы, символы и цифры. "\
        "Шрифты с флажком '🇷🇺' умеют обрабатывать текст на русском.\n\n"\
        "✔️ Все символы которые бот не сможет обработать не изменятся."

    photo = FILE_ID_IMAGE

    await state.clear()
    await state.set_state(States_bot.be_in_main_menu)

    if message:
        await message.answer_photo(photo=photo, caption=text,\
                                    reply_markup=main_menu_keyboard())
    elif callback:
        await callback.message.answer_photo(photo=photo, caption=text,\
                                            reply_markup=main_menu_keyboard())
    else:
        return


#Реакция на комманду /start
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await send_start_menu(message, None, state)


#Реакция на кнопку на главную
@start_router.callback_query(F.data=="back_button_to_main_menu")
async def back_click_to_main(callback: CallbackQuery, state: FSMContext):
    await callback.answer("✅ Возвращаемся на главную")

    if callback.message:
        try:
            await callback.message.delete()# удаление сообщения под которым была
        except Exception:                  # нажата кнопка "На главную" с проверкой
            pass                           # на существование этого сообщения

    await send_start_menu(None, callback, state)

#Oбработка кнопки Инфо
@start_router.callback_query(F.data == "info")
async def click_to_info(callback: CallbackQuery):
    await callback.answer("❔ Информация")

    try:
        await callback.message.delete() #удаляем главное меню
    except Exception:
        pass

    text = "🔩 Бот находится в разработке. Если заметишь ошибку, напиши: @KubikCode."

    await callback.message.answer(text, reply_markup=go_back_to_main_menu())