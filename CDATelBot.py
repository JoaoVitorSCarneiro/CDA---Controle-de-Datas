"""
Projeto de Controle de Datas Automático

João Vitor Soares Carneiro
"""

from aiogram import Bot
from INIT import BOT_TOKEN, CHAT_ID
import tracemalloc


async def start(text=None):
    """
    :param text: Texto a ser enviado pelo bot
    """
    text = text

    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text)
    finally:
        await bot.close()


tracemalloc.start()

if __name__ == '__main__':
    start()
