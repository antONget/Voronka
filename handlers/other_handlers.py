from aiogram import Router, F
from aiogram.types import Message
import logging
from aiogram.types import CallbackQuery

router = Router()


@router.message(F.photo)
async def process_start_command(message: Message) -> None:
    print(message.photo[3].file_id)

@router.callback_query(lambda callback: callback.data != 's')
async def callback_data(callback: CallbackQuery) -> None:
    logging.info(f'callback_data: {callback.data}')