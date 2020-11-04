#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging

# the Strings used for this "thing"
from translation import Translation

from pyrogram import (
    Client,
    Filters
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(Filters.command(["help", "about"]))
async def help_user(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(Filters.command(["start"]))
async def start(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )
