from aiogram.types import InlineKeyboardButton, CopyTextButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from routers.Simbols_process.utils_for_simbols import simbols_list



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
            text="На главную",
            callback_data="back_button_to_main_menu",
        )
    )
    return builder.as_markup()