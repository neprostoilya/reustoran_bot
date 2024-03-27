import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram import Bot

from config.configuration import URL
from handlers import commands, register, menu, cart, order, \
    information, events, settings
from config.instance import bot


async def on_startup(bot: Bot):
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Меню", web_app=WebAppInfo(url=URL + '/frontend/'))
    )


async def main():
    """ 
    Main 
    """
    dp = Dispatcher()
    
    dp.startup.register(on_startup)

    dp.include_routers(commands.router_commands)
    dp.include_routers(register.router_register)
    dp.include_routers(menu.router_menu)
    dp.include_routers(cart.router_cart)
    dp.include_routers(order.router_order)
    dp.include_routers(information.router_info)
    dp.include_routers(events.router_events)
    dp.include_routers(settings.router_settings)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())