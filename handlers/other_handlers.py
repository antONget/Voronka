from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.photo)
async def process_start_command(message: Message) -> None:
    print(message.photo[3].file_id)