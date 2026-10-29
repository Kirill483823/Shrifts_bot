import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher

from routers import get_routers

#.\.venv\Scripts\Activate.ps1
#source .venv/Scripts/activate






bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

for i in get_routers():
    dp.include_router(i)


async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
