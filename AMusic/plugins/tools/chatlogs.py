import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOG_GROUP_ID, AM_SUPPORT
from AMusic import app  
from AMusic.utils.database import get_served_chats



async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)
    
photo = [
    "https://graph.org/file/e3fd47b52279da5c302ef.jpg",
    "https://graph.org/file/e3fd47b52279da5c302ef.jpg",
    "https://graph.org/file/e3fd47b52279da5c302ef.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"🌹 ʙᴏᴛ ᴀᴅᴅᴇᴅ ᴛᴏ ɴᴇᴡ ɢʀᴏᴜᴘ ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ **ᴄʜᴀᴛ** › : {matlabi_jhanto}\n┣★ **ᴄʜᴀᴛ ɪᴅ** › : {chat_id}\n┣★ **ᴄʜᴀᴛ ᴜɴᴀᴍᴇ** › : {chatusername}\n┣★ **ᴛᴏᴛᴀʟ ᴄʜᴀᴛ** › : {served_chats}\n┣★ **ᴀᴅᴅᴇᴅ ʙʏ** › :\n┗━━━ {added_by}"
        await lul_message(AM_SUPPORT, lemda_text)
        

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ #𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ ✫\n✫ 𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n✫ 𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n✫ 𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n✫ 𝐁ᴏᴛ : @{app.username}"
        await app.send_message(AM_SUPPORT, left)
