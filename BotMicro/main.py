from os import getenv

from deta import Deta

from bot.factory import create_bot, create_dispatcher
from web.factory import create_app


BOT_TOKEN = getenv('BOT_TOKEN')
WEBHOOK_SECRET = getenv('WEBHOOK_SECRET')
assert BOT_TOKEN and WEBHOOK_SECRET, 'Set envs, baka!'


deta = Deta()

bot = create_bot(BOT_TOKEN)
dispatcher = create_dispatcher(deta)


app = create_app(
    deta,
    bot,
    dispatcher,
    WEBHOOK_SECRET
)
