from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from keyboards.keyboard_for_choose_fonts import create_choose_fonts
from States.bot_states import States_bot
from States.bot_states import States_for_pages
from errors_processing import error_answer
from routers.Font_process.utils_for_font_processing import shrifts_dict_page1, shrifts_dict_page2

processing_router = Router()

#Получение текста
@processing_router.message(States_bot.wait_send_text, F.text)
async def send_keyb_with_srifts(message: Message, state: FSMContext):

    await state.update_data(user_text=message.text)
    await state.set_state(States_for_pages.be_on_page1)

    data = await state.get_data()
    text = data["user_text"]

    await message.answer(text, reply_markup=create_choose_fonts(shrifts_dict_page1))


#Пользовател выбрал шрифт
@processing_router.callback_query(F.data.startswith("shrift:"))
async def text_processing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    message = callback.message
    callback_data = callback.data
    if not isinstance(message, Message) or callback_data is None:
        return

    data = await state.get_data()
    text = data.get("user_text")

    if text is None:
        await state.clear()
        try:
            await message.delete()
        except Exception:
            pass

        await error_answer(callback, text="⚠️ Текст не найден. Отправь новый.")
        return
    try: #try нужен на случай если пользователь нажал на туже кнопку два раза
        key = callback.data.split(':')[1]
        current_state = await state.get_state()
        fonts_dict = {
            States_for_pages.be_on_page1.state: shrifts_dict_page1,
            States_for_pages.be_on_page2.state: shrifts_dict_page2,
        }.get(current_state)

        if fonts_dict is None:
            await error_answer(callback)
            return
        if key not in fonts_dict:
            await error_answer(callback)
            return

        keyboard = create_choose_fonts(fonts_dict)
        await message.edit_text(fonts_dict[key](text), reply_markup=keyboard)

    except Exception as e:
        if "message is not modified" in str(e).lower():
        #"message is not modified" - это ошибка которая возникает
        #если пользователь нажал на туже кнопку два раза
            return
        else:
            await error_answer(callback)
