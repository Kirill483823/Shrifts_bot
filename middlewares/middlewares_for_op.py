from aiogram.types import Message, CallbackQuery
from aiogram import BaseMiddleware

from middlewares.keyboards_for_middleware import keyboard_for_OP
from middlewares.functions_for_middleware import is_subscribe


channel_id = -1002079572984

text = "☝️ Чтобы пользоваться ботом, подпишись на канал спонсора. Благодаря этому бот может оставаться бесплатным.\n\n" \
    "⚠️ После подписки подожди около 10 секунд, затем нажми любую кнопку ещё раз."

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
                await event.answer(text="Подожди 10 секунд, пока статус подписки обновится.", show_alert=True)

                try: #пытаемся изменить текст
                    await event.message.edit_text(text, reply_markup=keyboard_for_OP())

                except Exception:
                    await event.message.answer(text, reply_markup=keyboard_for_OP())

            return
