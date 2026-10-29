from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, CopyTextButton




def create_choose_fonts(shrifts_dict: dict, user_text: str | None):
    builder = InlineKeyboardBuilder()
    default_text = "Example"

    """Генератор кнопок для выбора шрифтов"""
    for key, func in shrifts_dict.items():

        text=func(default_text)

        if text == None or text == "":  #проверка на то что вернула функция для текста
            text = "Ошибка"             #кнопкпи, в кнопке не может быть None | ""

        builder.button(text=text, callback_data=f"shrift:{key}")


    builder.adjust(2)

    if user_text:
        builder.row(
            InlineKeyboardButton(
                text = "Копировать",
                copy_text = CopyTextButton(text = user_text)
            ))


    builder.row(InlineKeyboardButton( text="☚", callback_data="go_to_before_page"),
        InlineKeyboardButton(text = "☛", callback_data="go_to_next_page"))

    builder.row(InlineKeyboardButton(text="📖 На главную", callback_data="back_button_to_main_menu"),
    InlineKeyboardButton(text="🆕 Новый текст", callback_data="accept_text"))

    return builder.as_markup()
