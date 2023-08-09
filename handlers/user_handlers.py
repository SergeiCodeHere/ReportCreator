from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU['/start'])


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['/help'])


@router.message(Text(text=['Отчет']))
async def cal_choose(message: Message):
    await message.answer('Введите дату в формате: день.месяц.год')
