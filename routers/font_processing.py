from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from keyboards.keyboard_for_choose_fonts import create_choose_fonts
from States.bot_states import States_bot
from errors_processing import error_answer
from routers.Utils_for_font_processing import shrifts_dict

processing_router = Router()

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
