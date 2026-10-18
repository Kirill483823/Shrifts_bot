from typing import Awaitable, Any, Dict, Callable
from aiogram.types import TelegramObject, Message, CallbackQuery
from aiogram import BaseMiddleware, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from cashews import cache
import asyncio
from errors_processing import error_answer

channel_id = -1002079572984
states = {"member", "administrator", "creator"}


async def is_subscribe(bot: Bot,
                       chat_id,
                       user_id):

    cache_key = f"sub:{chat_id}:{user_id}"  # 1. Создаём «адрес» для хранения результата
    cashed = await cache.get(cache_key)     # 2. Смотрим в кэш, есть там True для этого пользователя?

    if cashed is not None:
        return cashed

    try:
        member = await bot.get_chat_member(channel_id, user_id)
        is_subscribed =  member.status in states
    except Exception:
        is_subscribed = False

    if is_subscribed:
        ttl = "5m"
    else:
        ttl = "10s"

    await cache.set(cache_key, is_subscribed, expire=ttl)
    return is_subscribed






text ="☝️ Чтобы поьзоваться ботом надо подписаться на споносоров, благодаря этому бот работает бесплатно.\n \n " \
            "Статус обновится автоматически через 10 секунд после подписки. Просто подожди и нажми любую кнопку снова"

def keyboard_for_OP():
    builder = InlineKeyboardBuilder()
    builder.button(text = "Подписаться", url =  "https://t.me/YablokoSerials")
    builder.button(text = "Я подписался", callback_data = "back_button_to_main_menu")
    builder.adjust(1)
    return builder.as_markup()

class OP_middleWare(BaseMiddleware):
    def __init__(self, bot):
        self.bot = bot

    async def __call__(self, handler, event, data):
        user = getattr(event, "from_user", None)
        #Это очень удобная и «безопасная» строчка кода, которая говорит: «Попробуй достать из события
        #поле from_user, но если его там нет — не ломай программу, а просто верни None».

        if not user or user.is_bot: #если нет вообще поля from_user или в поле user.is_bot (=True)
            return await handler(event, data)#пропускаем

        #если подписан
        if await is_subscribe(self.bot, channel_id, user.id):
                return await handler(event, data)

        #если не подписан
        else:
            if isinstance(event, Message): #Message - это событие, которое возникает, когда пользователь отправляет сообщение боту.
                await event.answer(text, reply_markup= keyboard_for_OP())

            elif isinstance(event, CallbackQuery): #CallbackQuery - это событие, которое возникает, когда пользователь нажимает на кнопку в сообщении бота.
                await event.answer(text="Подожди 10 секунд пока статус обновиться.", show_alert=True)

                try: #пытаемся изменить текст
                    await event.message.edit_text(text, reply_markup=keyboard_for_OP())

                except Exception:
                    await event.message.answer(text, reply_markup=keyboard_for_OP())
            return
