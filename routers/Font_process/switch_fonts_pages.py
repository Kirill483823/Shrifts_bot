from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from States.bot_states import States_for_pages
from keyboards.keyboard_for_choose_fonts import create_choose_fonts
from routers.Font_process.utils_for_font_processing import shrifts_dict_page2
from routers.Font_process.utils_for_font_processing import shrifts_dict_page1

from errors_processing import error_answer

font_process_router = Router()

"""Тексты для ошибок при переходе на страницы"""
text = "⚠️ Произошла ошибка при переходе на следующую страницу. Попробуйте снова."


@font_process_router.callback_query(F.data == "go_to_next_page")
async def go_to_next_page(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    message = callback.message
    if not isinstance(message, Message):
        return

    try:
        await message.edit_reply_markup(
            reply_markup=create_choose_fonts(shrifts_dict_page2, message.text)
        )
        await state.set_state(States_for_pages.be_on_page2)
    except Exception as e:
        if "message is not modified" in str(e).lower():
            return
        else:
            await error_answer(callback, text=text)

@font_process_router.callback_query(F.data == "go_to_before_page")
async def go_to_before_page(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    message = callback.message
    if not isinstance(message, Message):
        return

    try:
        await message.edit_reply_markup(
            reply_markup=create_choose_fonts(shrifts_dict_page1, message.text)
        )
        await state.set_state(States_for_pages.be_on_page1)
    except Exception as e:
        if "message is not modified" in str(e).lower():
            return
        else:
            await error_answer(callback, text=text)