import asyncio 
from aiogram import Bot, Dispatcher
from msg_handler import r

async def main():
    dp = Dispatcher()
    dp.include_router(r)

    bot = Bot(token=open("BOT_TOKEN.txt").readline())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())