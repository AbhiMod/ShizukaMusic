import random
from pyrogram import filters
from pyrogram.types import Message
from AMusic import app
from AMusic.core.call import Inflex
from AMusic.utils import bot_sys_stats
from AMusic.utils.decorators.language import language
from AMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
from io import BytesIO
from pyrogram import filters
from typing import Union
from AMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AMusic.core.userbot import assistants

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await Inflex.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    resp = (datetime.now() - start).microseconds / 1000
    text =  "🏓 𝖯𝗈𝗇𝗀 : {0}ᴍs\n\n{1} 𝖲𝗒𝗌𝗍𝖾𝗆 𝖲𝗍𝖺𝗍𝗌 :\n\n↬ 𝖴𝗉𝖳𝗂𝗆𝖾 : {2}\n↬ 𝖱𝖠𝖬 : {3}\n↬ 𝖢𝖯𝖴 : {4}\n↬ 𝖣𝗂𝗌𝗄 : {5}\n↬ 𝖯𝗒-𝖳𝗀𝖼𝖺𝗅𝗅𝗌 : {6}ᴍs\n↬ ꜱᴇʀᴠᴇʀ ᴄʜᴀᴛꜱ : {7}\n↬ ꜱᴇʀᴠᴇʀ ᴜꜱᴇʀꜱ : {8}\n↬ ᴀꜱꜱɪꜱ ɪᴅꜱ : {9}".format(resp, app.name, UP, RAM, CPU, DISK, pytgping, served_chats, served_users,len(assistants))
    carbon = await make_carbon(text)
    await message.reply_photo((carbon),
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+",
            )
        
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"close"
            )
        ],
    ]
    ),
        )
