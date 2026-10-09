from aiogram.utils.keyboard import InlineKeyboardBuilder




def create_choose_fonts(shrifts_dict: dict):
    builder = InlineKeyboardBuilder()
    default_text = "Example"

    """Генератор кнопок для выбора шрифтов"""
    for key, func in shrifts_dict.items():

        text=func(default_text)
        if text == None or text == "":  #проверка на то что вернула функция для текста
            text = "Ошибка"             #кнопкпи, в кнопке не может быть None | ""

        builder.button(text=text, callback_data=f"shrift:{key}")

    builder.button(text="📖 На главную", callback_data="back_button_to_main_menu")
    builder.button(text="🆕 Новый текст", callback_data="accept_text")
    builder.adjust(2)
    return builder.as_markup()