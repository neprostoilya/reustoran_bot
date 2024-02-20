from aiogram.utils.keyboard import ReplyKeyboardBuilder, WebAppInfo, InlineKeyboardBuilder
from config.configuration import URL


def open_web_menu_kb(token):
    """
    Open web menu keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text='Интерактивное меню',
        web_app=WebAppInfo(url=URL + '/frontend/' + str(token)),
        url=''
    )

    return builder.as_markup(
        resize_keyboard=True
    )

def main_menu_kb():
    """
    Main menu keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text='🍽 Меню')
    builder.button(text='🛒 Корзина')
    builder.button(text='📖 Мои заказы')
    builder.button(text='🎊 Акции')
    builder.button(text='☎️ Обратная связь')
    builder.button(text='⚙️ Настройки')

    builder.adjust(1, 2, 2, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


def back_to_main_menu_kb():
    """
    Back to Main menu keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text='⬅️ Главное меню')

    return builder.as_markup(
        resize_keyboard=True
    )
