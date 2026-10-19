
from aiogram.utils.keyboard import InlineKeyboardBuilder

def keyboard_for_OP():
    builder = InlineKeyboardBuilder()
    builder.button(text = "☑️ Подписаться", url =  "https://t.me/YablokoSerials")
    builder.button(text = "✅ Проверить подписку", callback_data = "back_button_to_main_menu")
    builder.adjust(1)
    return builder.as_markup()