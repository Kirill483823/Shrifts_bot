from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from aiogram.filters import StateFilter

from keyboards.keyboard_for_choose_fonts import create_choose_fonts
from States.bot_states import States_bot
from config import FILE_ID_FOR_WAITING_TEXT

processing_router = Router()

import fancify_text
shrifts_dict = fonts_map_funcs = { #список функций преобразователей
    "sans_serif": fancify_text.sansSerif,
    "bold": fancify_text.bold,
    "italic": fancify_text.italic,
    "bold_italic": fancify_text.boldItalic,
    "monospace": fancify_text.monospaced,
    "wide": fancify_text.wide,
    "bold_serif": fancify_text.boldSerif,
    "script": fancify_text.script,
    "fraktur": fancify_text.fraktur,
    "double_struck": fancify_text.doubleStruck,
    "boxed": fancify_text.boxed,
    "currency": fancify_text.currency,
    "blue": fancify_text.blue,
    "blue": fancify_text.blue,
    "smallCaps": fancify_text.smallCaps,
    "curly": fancify_text.curly,
    "reversed_": fancify_text.reversed_,
    "upsideDown": fancify_text.upsideDown,
    "boxed": fancify_text.boxed,
    "wiry": fancify_text.wiry,
    "parenthesized": fancify_text.parenthesized,
    "heavyCircled": fancify_text.heavyCircled,
    "currency": fancify_text.currency,
    "cool": fancify_text.cool,
    "magic": fancify_text.magic,
}

"""Oтвет в случае ошибки"""
async def error_answer(callback: CallbackQuery):
    await callback.message.answer("⚠️ Ошибка, попробуйте перезапустить бота")

"""Обработка нажатия на кнопку 'Oтправить текст' и 'новый текст'"""
@processing_router.callback_query(F.data == "accept_text")

async def waiting_text(callback: CallbackQuery, state: FSMContext):

    await state.clear()
    await state.set_state(States_bot.wait_send_text)

    photo = FILE_ID_FOR_WAITING_TEXT
    text = "❇️ Просто тправте текст:\n\n⚠️Использовать можно любые буквы, символы, цифры,"\
           " но обработаются только латинские (английские) буквы и цифры,"\
           " всё остальное останется без изменений.\n"

    await callback.answer()
    try:
        await callback.message.delete()
    except Exception:
        pass

    await callback.message.answer_photo(photo=photo, caption=text)

"""Получение текста"""
@processing_router.message(States_bot.wait_send_text, F.text)
async def send_keyb_with_srifts(message: Message, state: FSMContext):

    await state.update_data(user_text=message.text)
    await state.set_state(States_bot.choosen_shrifts)

    data = await state.get_data()
    text = data["user_text"]

    await message.answer(text, reply_markup=create_choose_fonts(shrifts_dict))

@processing_router.callback_query(F.data.startswith("shrift:"))
async def text_processing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    text = data.get("user_text")

    if text is None:
        await error_answer(callback)
        return

    try: #это если поьзователь нажал на туже кнопку два раза
        key = callback.data.split(':')[1]
        await callback.message.edit_text(shrifts_dict[key](text), reply_markup=create_choose_fonts(shrifts_dict))

    except Exception as e:
        if "message is not modified" in str(e).lower():
            return
        else:
            await error_answer(callback)