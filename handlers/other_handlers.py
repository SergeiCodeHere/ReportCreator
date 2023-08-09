from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message()
async def process_another_commands(message: Message):
    await message.reply(LEXICON_RU['another'])
