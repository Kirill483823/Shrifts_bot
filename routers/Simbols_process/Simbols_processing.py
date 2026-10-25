from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F, Router

from States.bot_states import States_bot
from keyboards.keyboard_for_choosen_simbols import create_chose_simbols
from routers.Simbols_process.utils_for_simbols import simbols_list
from errors_processing import error_answer

simbols_router = Router()

#Обработка нажатия на кнопку 'Unicode-Символы'
@simbols_router.callback_query(F.data == "Unicode_simbols", States_bot.be_in_main_menu)
async def unicode_simbols(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Выбери символ из списка", reply_markup=create_chose_simbols(simbols_list, None))

@simbols_router.callback_query(F.startswith("simbol:"))
async def simbol(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    chosen_simbol = callback.data.split(":")[1]

    try:
        await callback.message.edit_text(text = chosen_simbol, reply_markup=create_chose_simbols(simbols_list, chosen_simbol))

    except Exception as e:
        if "message is too long" in str(e):
            pass
        else:
            await error_answer(callback)
