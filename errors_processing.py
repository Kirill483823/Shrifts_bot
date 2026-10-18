
from aiogram.types import CallbackQuery
from keyboards.errors_keyboards import unknown_error


async def error_answer(callback: CallbackQuery, text: str = "⚠️ Ошибка, попробуйте перезапустить бота."):
    await callback.message.answer(text, reply_markup=unknown_error())