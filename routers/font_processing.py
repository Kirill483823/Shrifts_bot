from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from keyboards.keyboard_for_choose_fonts import create_choose_fonts
from States.bot_states import States_bot
from config import FILE_ID_FOR_WAITING_TEXT
from errors_processing import error_answer

processing_router = Router()

import fancify_text
shrifts_dict = { #список функций преобразователей
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


#Обработка нажатия на кнопку 'Oтправить текст' и 'новый текст'
#и ожидание текста от пользователя
@processing_router.callback_query(F.data == "accept_text")
async def waiting_text(callback: CallbackQuery, state: FSMContext):

    await state.clear()
    await state.set_state(States_bot.wait_send_text)

    photo = FILE_ID_FOR_WAITING_TEXT
    text = (
        "❇️ Просто отправь текст:\n\n⚠️ Можно использовать любые буквы, символы и цифры, "
        "но будут обработаны только латинские (английские) буквы и цифры. "
        "Остальные символы останутся без изменений."
    )

    await callback.answer()
    try:
        await callback.message.delete()
    except Exception:
        pass

    await callback.message.answer_photo(photo=photo, caption=text)

#Получение текста
@processing_router.message(States_bot.wait_send_text, F.text)
async def send_keyb_with_srifts(message: Message, state: FSMContext):

    await state.update_data(user_text=message.text)
    await state.set_state(States_bot.choosen_shrifts)

    data = await state.get_data()
    text = data["user_text"]

    await message.answer(text, reply_markup=create_choose_fonts(shrifts_dict))

#Пользовател выбрал шрифт
@processing_router.callback_query(F.data.startswith("shrift:"))
async def text_processing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    text = data.get("user_text")

    if text is None:
        await state.clear()#потому что так сказала нейронка
        try:#Для того чтобы не вылезла ошибка, хз как поьзователь может её вызвать кнчн
            await callback.message.delete()
        except Exception:
            pass

        await error_answer(callback, text="⚠️ Текст не найден. Отправь новый.")
        return

    try: #try нужен на случай если пользователь нажал на туже кнопку два раза
        key = callback.data.split(':')[1]
        keyboard = create_choose_fonts(shrifts_dict)
        await callback.message.edit_text(shrifts_dict[key](text), reply_markup=keyboard)

    except Exception as e:
        if "message is not modified" in str(e).lower():
        #"message is not modified" - это ошибка которая возникает
        #если пользователь нажал на туже кнопку два раза
            return
        else:
            await error_answer(callback)
