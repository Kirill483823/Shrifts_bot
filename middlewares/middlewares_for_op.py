from typing import Awaitable, Any, Dict, Callable
from aiogram.types import TelegramObject, Message, CallbackQuery
from aiogram import BaseMiddleware, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder



#проврка какой статус у пользователя в чате (подписан ли он на канал или нет)
async def is_subscribed(bot: Bot, chat_id: int | str, user_id: int) -> bool:
    states_in_chat = {"member", "administrator", "creator"}

    member = await bot.get_chat_member(chat_id, user_id)
    #member это экземпляр класса ChatMember,
    #который содержит информацию о пользователе в чате

    return member.status in states_in_chat

def OP_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Подписаться", url = "https://t.me/YablokoSerials")
    builder.button(text="✅ Я подписался", callback_data="back_button_to_main_menu")
    builder.adjust(1)
    return builder.as_markup()

text = "☝️ Чтобы поьзоваться ботом надо подписаться на споносоров, благодаря этому бот работает бесплатно." \
            "После подписки нажмите на кнопку 'Я подписался' и продолжайте пользоваться ботом."

class OP_middleware(BaseMiddleware):

        async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event:TelegramObject, #Здесь хранятся все данные от пользователя: текст сообщения (event.text), ID чата (event.chat.id), имя пользователя (event.from_user.username) и т.п.
        data: Dict[str, Any]
    ) -> Any:
            if isinstance(event, (Message, CallbackQuery)):
                user_id = event.from_user.id
            else:
                 return None
            try:
                if await is_subscribed(event.bot, "@YablokoSerials", user_id):
                    return await handler(event, data)
            except Exception:
                return None

            else:#если пользователь не подписан на канал
                if isinstance(event,Message): #если пользователь отправил что-то
                    await event.answer(text=text, reply_markup=OP_keyboard())

                elif isinstance(event, CallbackQuery):#если пользователь нажал на кнопку
                    await event.answer()
                    try:
                        await event.message.edit_text(text=text, reply_markup=OP_keyboard())
                    except Exception:
                        await event.message.answer(text=text, reply_markup=OP_keyboard())
