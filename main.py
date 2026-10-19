import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from cashews import cache

from routers import get_routers
from middlewares.middlewares_for_op import OP_middleWare

#.\.venv\Scripts\Activate.ps1
#source .venv/Scripts/activate

cache.setup("mem://") #создаем хронилище кэша для ОП в оперативной памяти

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
op_middleware = OP_middleWare(bot)
dp.message.outer_middleware(op_middleware)
dp.callback_query.outer_middleware(op_middleware)


for i in get_routers():
    dp.include_router(i)


async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
