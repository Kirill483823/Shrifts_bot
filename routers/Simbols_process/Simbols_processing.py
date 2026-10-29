from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from States.bot_states import States_bot
from keyboards.keyboard_for_choosen_simbols import create_chose_simbols
from routers.Simbols_process.utils_for_simbols import simbols_list_page_1, simbols_list_page_2
from errors_processing import error_answer
from States.bot_states import States_for_pages_for_simbols

simbols_router = Router()

#Обработка нажатия на кнопку 'Unicode-Символы'
@simbols_router.callback_query(F.data == "Unicode_simbols", States_bot.be_in_main_menu)
async def unicode_simbols(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(chosen_simbol=None)
    await state.set_state(States_for_pages_for_simbols.page_1_for_simbols)
    await callback.message.answer("Выбери символ из списка",
                                  reply_markup=create_chose_simbols(simbols_list_page_1, None))


@simbols_router.callback_query(F.data == "go_to_next_page_with_simbols")
async def go_to_next_simbols_page(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    message = callback.message
    if not isinstance(message, Message):
        return

    data = await state.get_data()
    try:
        await message.edit_reply_markup(
            reply_markup=create_chose_simbols(simbols_list_page_2, data.get("chosen_simbol"))
        )
        await state.set_state(States_for_pages_for_simbols.page_2_for_simbols)
    except Exception as e:
        if "message is not modified" not in str(e).lower():
            await error_answer(callback)


@simbols_router.callback_query(F.data == "go_to_before_page_with_simbols")
async def go_to_before_simbols_page(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    message = callback.message
    if not isinstance(message, Message):
        return

    data = await state.get_data()
    try:
        await message.edit_reply_markup(
            reply_markup=create_chose_simbols(simbols_list_page_1, data.get("chosen_simbol"))
        )
        await state.set_state(States_for_pages_for_simbols.page_1_for_simbols)
    except Exception as e:
        if "message is not modified" not in str(e).lower():
            await error_answer(callback)


#Обработка нажатия на символ
@simbols_router.callback_query(F.data.startswith("simbol:"))
async def simbol(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    message = callback.message
    callback_data = callback.data
    if not isinstance(message, Message) or callback_data is None:
        return

    chosen_simbol = callback_data.partition(":")[2]
    current_state = await state.get_state()
    simbols_list = (
        simbols_list_page_2
        if current_state == States_for_pages_for_simbols.page_2_for_simbols.state
        else simbols_list_page_1
    )
    await state.update_data(chosen_simbol=chosen_simbol)

    try:
        await message.edit_text(
            text=chosen_simbol,
            reply_markup=create_chose_simbols(simbols_list, chosen_simbol),
        )

    except Exception as e:
        if "message is not modified" not in str(e).lower():
            await error_answer(callback)