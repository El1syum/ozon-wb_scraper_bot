import logging

from aiogram import types, Dispatcher

from scripts.ozon.get_count import get_ozon_count
from scripts.wildberries.get_count import get_wb_count


async def get_count(message: types.Message):
    logging.info(message)
    query = message.text
    await message.reply('Запрос принят, секунду...')
    wb_count = get_wb_count(query)
    ozon_count = get_ozon_count(query)
    await message.answer(f'Результаты по запросу {query}')
    await message.answer(f'Ozon: {ozon_count}')
    await message.answer(f'Wildberries: {wb_count}')


def register_get_count(dp: Dispatcher):
    dp.register_message_handler(get_count)
