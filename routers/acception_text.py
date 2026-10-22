from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from States.bot_states import States_bot
from config import FILE_ID_FOR_WAITING_TEXT
from keyboards.keyboard_for_choose_fonts import create_choose_fonts

accept_text_router = Router()

#Обработка нажатия на кнопку 'Oтправить текст' и 'новый текст'
#и ожидание текста от пользователя
@accept_text_router.callback_query(F.data == "accept_text")
async def waiting_text(callback: CallbackQuery, state: FSMContext):

    await state.clear()
    await state.set_state(States_bot.wait_send_text)

    photo = FILE_ID_FOR_WAITING_TEXT
    text = (
        "❇️ Просто отправь текст:\n\n⚠️ Можно использовать любые буквы, символы и цифры. "
        "Шрифты с флажком '🇷🇺' умеют обрабатывать текст на русском. "\
        "Все символы которые бот не сможет обработать не изменятся"
    )

    await callback.answer()
    try:
        await callback.message.delete()
    except Exception:
        pass

    await callback.message.answer_photo(photo=photo, caption=text)