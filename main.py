from os import getenv

from aiogram_deta.web import create_app
from deta import Deta

from bot.factory import create_bot, create_dispatcher


BOT_TOKEN = getenv('BOT_TOKEN')
assert BOT_TOKEN

WEBHOOK_SECRET = getenv('WEBHOOK_SECRET')
assert WEBHOOK_SECRET

deta = Deta()

bot = create_bot(BOT_TOKEN)
dispatcher = create_dispatcher(deta)

app = create_app(
    deta,
    bot,
    dispatcher,
    WEBHOOK_SECRET
)
