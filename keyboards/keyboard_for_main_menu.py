from aiogram.utils.keyboard import InlineKeyboardBuilder
#кнопки галвного меню
def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🆕 Отправить текст", callback_data="accept_text")
    builder.button(text="ℹ️ Инфо", callback_data="info")
    builder.button(text="👑 Наш канал", url="https://t.me/YablokoSerials")
    builder.adjust(2)
    return builder.as_markup()

#кнопки в 'Инфо'
def go_back_to_main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📖 Назад", callback_data="back_button_to_main_menu")
    builder.button(text="👑 Наш канал", url="https://t.me/YablokoSerials")
    builder.adjust(1)
    return builder.as_markup()
