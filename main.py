import asyncio
import json
import logging
import requests

from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher,types, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


from handlers.main_hand import router as router6
from handlers.support import router as router4
from handlers.buy import router as router1
from handlers.date import router as router2
from handlers.geo import router as router3
from handlers.referal import router as router5

load_dotenv()


async def fetch_data():
    while True:
        get = requests.get(os.getenv("DATA_API"))

        data = get.text

        with open("json/data.json", "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("данные на месте")
        await asyncio.sleep(500)

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(router1, router2, router3, router4, router5, router6)
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(
        dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()),
        fetch_data()
    )



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
