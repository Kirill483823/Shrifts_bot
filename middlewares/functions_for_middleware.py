from cashews import cache
from aiogram import Bot

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
