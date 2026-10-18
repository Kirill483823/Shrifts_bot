from keyboards.errors_keyboards import unknown_error
from aiogram.types import CallbackQuery


async def error_answer(callback: CallbackQuery, text: str = "⚠️ Ошибка, попробуйте перезапустить бота."):
    await callback.answer()
    await callback.message.answer(text, reply_markup=unknown_error())
