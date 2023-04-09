from os import getenv

from deta import Deta

from bot.factory import create_bot, create_dispatcher
from web.factory import create_app


BOT_TOKEN = getenv('BOT_TOKEN')
assert BOT_TOKEN


deta = Deta()

bot, webhook_secret = create_bot(BOT_TOKEN)
dispatcher = create_dispatcher(deta)


app = create_app(
    deta,
    bot,
    dispatcher,
    webhook_secret
)
