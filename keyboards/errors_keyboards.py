from aiogram.utils.keyboard import InlineKeyboardBuilder

#клавиатуры для ошибок
def unknown_error():
    builder = InlineKeyboardBuilder()
    builder.button(text="🆕 Задать новый текст", callback_data="accept_text")
    builder.button(text="📖 На главную", callback_data="back_button_to_main_menu")
    builder.adjust(1)
    return builder.as_markup()