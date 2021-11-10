import heroku3
from functools import wraps

from bot import HEROKU_API, HEROKU_APP

# Preparing For Setting Config
# Implement by https://github.com/jusidama18 and Based on this
# https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/heroku_helpers.py

heroku_client = heroku3.from_key(HEROKU_API) if HEROKU_API else None


def check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text(
                "`Please Add HEROKU_API Key For This To Function To Work!`",
                parse_mode="markdown"
            )
        elif not HEROKU_APP:
            await message.reply_text(
                "`Please Add HEROKU_APP For This To Function To Work!`",
                parse_mode="markdown"
            )
        if HEROKU_APP and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP)
            except BaseException:
                await message.reply_text(
                    message,
                    "`Heroku Api Key And App Name Doesn't Match!`",
                    parse_mode="markdown"
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli