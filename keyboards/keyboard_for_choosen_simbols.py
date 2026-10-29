from aiogram.types import InlineKeyboardButton, CopyTextButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_chose_simbols(simbols_list: list, chosen_simbol: str | None):
    builder = InlineKeyboardBuilder()

    for i in simbols_list: #кнопки для каждого символа
        builder.button(text=i, callback_data=f"simbol:{i}")

    builder.adjust(4)
    if chosen_simbol is not None:
        builder.row(InlineKeyboardButton(
            text = "Копировать",
            copy_text = CopyTextButton(text = chosen_simbol)

        ))

    builder.row(
        InlineKeyboardButton(
            text="☚",
            callback_data="go_to_before_page_with_simbols"),
        InlineKeyboardButton(
            text="☛",
            callback_data="go_to_next_page_with_simbols"
        ))


    builder.row(
        InlineKeyboardButton(
            text="На главную",
            callback_data="back_button_to_main_menu",
        )
    )
    return builder.as_markup()