from os import getenv

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    project_host = getenv('DETA_SPACE_APP_HOSTNAME')
    await message.answer(f'Hello from {project_host}!' if project_host else '4$110! (error)')
