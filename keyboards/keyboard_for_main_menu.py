from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

#кнопки галвного меню
def main_menu_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text="🆕 Отправить текст",
            callback_data="accept_text",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="Unicode-Символы",
            callback_data="Unicode_simbols",
        )
    )
    builder.row(
        InlineKeyboardButton(text="ℹ️ Инфо", callback_data="info"),
        InlineKeyboardButton(
            text="👑 Наш канал",
            url="https://t.me/YablokoSerials"
        )
    )
    return builder.as_markup()

#кнопки в 'Инфо'
def go_back_to_main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📖 Назад", callback_data="back_button_to_main_menu")
    builder.button(text="👑 Наш канал", url="https://t.me/YablokoSerials")
    builder.button(text="Поддержать разработчика", url="https://pay.cloudtips.ru/p/94f58396")
    builder.adjust(1)
    return builder.as_markup()
