# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Channel-Message-Editor/blob/main/LICENSE

import os
import pyrogram
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
CHAT_IDS = list(set(int(x) for x in os.environ.get("CHAT_IDS", None).split()))
EDIT_FORMAT = os.environ.get("EDIT_FORMAT")

FayasNoushad = Client(
    "Channel Message Editor",
    session_name = os.environ["SESSION_STRING"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

@FayasNoushad.on_message(filters.caption & filters.channel)
async def edit_caption(client, message):
    try:
        if LOG_CHANNEL:
            await message.forward(LOG_CHANNEL)
            return
        if int(message.chat.id) in CHAT_IDS:
            await client.edit_message_caption(
                chat_id=message.chat.id,
                message_id=message.message_id,
                caption=EDIT_FORMAT.format(message.text)
            )
    except FloodWait as floodwait:
        await asyncio.sleep(floodwait.x)
        return edit_caption(client, message)
    except Exception as error:
        print(error)


FayasNoushad.run()
