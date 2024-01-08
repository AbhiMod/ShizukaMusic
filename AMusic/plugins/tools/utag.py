from AMusic import app 
import random
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
import traceback
from pyrogram import Client, filters

STRING = os.environ.get("STRING", "BQBLlUGAKtdNjrrYweOhQ6uzmCFdQNufaKxCB12q3P6kajlwn59Vmn3wqRBj9pZZMmbhAdE0jt-CRE3bxCtLnTmikA7x8FkcF_Uap2t7WhS4DbMdjX_HgEhBg8ylNNr2oIwkAEaIHGv1W2aRMBhh2zhDWAZfiuswSQI8cDuL0GABoikIhGUZ6TFdWbpIZz2FYWn6765l-bO1Se2pCIZpfAIRpq3cFabkYv5D_Ucvs6zQnAMyPkKrSVycSsRaKI1gg2tDFyr-PLj7tMe0tdcgdmrmNH4xlEa_JY5V_9kYg38OEYXBLBxrlo8DaJm5KKfST4vR_tvywD3fBWWAbH5gS4LsHBZZ_wA")
API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"
client = Client(STRING, API_ID, API_HASH)

SPAM_CHATS = []
TAGMES = [ " Hey Baby Kaha Ho 🥱🥺",
           " Oye So Gye Kya Online Aao Na 😊",
           " Vc Chalo Bate Karte Hain Kuch Kuch 😃 ",
           " Khana Kha Liya Ji ..??🥲 ",
           " Ghar MeSab Kaise Hai Ji 🥺",
           " Aapko Pata He Me Aapko Bahut Miss Karrahi Thi 🤭🙈",
           " Oye HaalChal Kaise He..??🤨 ",
           " Mere Se Setting Karoge ..??🙂 ",
           " Aapka Nama Kya he ..??🥲 ",
           " Naasta Huw Aapka ..??😋",
           " Mere Ko Apne Group Me Kidnap Karlo Na 😍 ",
           "𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅 ",
           "Mere Se Dosti Karoge..??🤔 ",
           " Sone Chale Gaya Kya 🙄🙄 ",
           " Aap Kaha Se Ho..??🙃 ",
           " Hello Ji Namaste 😛 ",
           " Hello Kkrh ..?🤔",
           " Do You Know Who Is My Owner.?😜😜 ",
           " Aur Batao Kaise Ho 😇 ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " Mere Se Baat Noi Katoge 🥺🥺",
           " Oye Pagal Online Aa ja 😶 ",
           " Oye Good Morning  😜",
           " Suno Ek Kaam Hai Tumse 🙂 ",
           " Nice To Meet Uh ☺ ",
           " Hello 🙊 ",
           " Bolo Na Kuch Yrr 🥲 ",
           " Tiger Queen Kon Hai...??😅 ",
           " Tumari Ek Pic Milgai ..?😅",
           " Mummy Aa Gyi Kya 😆😆😆",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " Do You Love Me ..?👀🙉",
           " Ek Song Sunau Na Pls ..😻😻 ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " Sara Kaam Khatam Hogaya Kya aapka ..?🙃",
           " Kaha Se Ho Aap 😊 ",
           " Sunno Na 🧐🧐 ",
           " Mera Ek Kaam Kardo Ge..?** ",
           " Kya Huw ..?👱 ",
           "Bahut Yaad Aarahe ho  🤧❣️ ",
           " U Bhul gaya Mujte 😏😏",
           " Jut Nahi Bolna Chaya Yrr  🤐 ",
           "Kha Lo Bhaw Matt Karo Baat 😒😒 ",
           " Hii 👀",
           " Aaj Mai Sad Hu ☹️ ",
           " Mujse V Cat Karlo Na 🥺🥺",
           " Kya Karr Rahe Ho 👀",
           " Kya Hal Chaal Hai 🙂",
           " Kaha Se Ho Aap..?🤔** ",
           " Chatt Karlo Na Group Me Mujse..🥺🥺",
           " Me Masoom Hu Thoda Sa 🥺🥺",
           " Kal Maja Aaya Tha Na 🤭😅 ",
          """Ek Jokes For U 🤭🤭
          
beta - pita ji, aap bahut kismat vaale hain? 
pita jee - vo kaise beta? 
beta - kyonki main fail ho gaya hoon.
aapako mere liye nai kitaaben nahin kharidani padengi.
💕💕💕💕💕💕""",
          """[EK Song AapKe Liya 🥺🥺](t.me/sam_loveall)
          
Ye jo halka halka suroor hai
Ye teri nazar ka kusoor hai
Ke sharaab peena sikha diya
Tere pyaar ne teri chaah ne
Teri behki behki nigaah ne
Mujhe ek sharaabi bana diya
k sharab peena sikha diya
💕💕💕💕💕💕💕💕💕💕
""",
          "Me Telegram Delete Karne Wali Hu 🥺", 
          "Aapka Pata He Kya Group Ka Owner kON hE",
          "oii Date Pe Chalega Mere Sath..?🤭🙉",
          "U Gannda Bachha Online Nahi Aate 🤭",
          "Mera break up Hogaya Aaj 💔😣",
          "Thoda Meri tarif Kardo Na 🤭🙉",
          "Me AapKo Janti HuNa 😳",
          "Me Dekhrahi hu 👀👀",
          "Tumara V break up Hogaya He Kya ",
          "AapKo Achha Nahi Laga Vc Pe 🥺",
          "Suggest Kardo Na Group Me Kese Baad Karu ",
          "Chiiii 🤧",
          "[Kon He Jaante Ho Kya 🤧](t.me/sam_loveall)",
          "AajKal Tum Bahut Ignore Karte Ho HamKo 🤔",
          "Thoda Der Pehle Tumse Pyar Huw Ussi Time break up V Hogaya 🤭🤭",
          "Dekho Kese Kese Log He Ider 🤭",
          "Kya Huw Aapko 🥺🥺",
          "Muje AapSe Baat Nahi Karni 🥺",
          "Aapko Pata He Mere pass 10+ Dil He Ek Aapka V He 🤭",
          "Me JarahiHu 💔😣",
          "chalo Chalte He 🤭 ",
          "U 💔💔💔💔💔💔",
          
          
           ]


#TagOffBot

@client.on_message(
    filters.command(["cancel", "stopall", "off"], prefixes=["/", ".", "?", "-", "", "!"])
    & filters.group
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ["administrator", "creator"]:
        return await message.reply_text("**Only admins can use this command!**")

    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
            off = random.choice(Ca)
        return await message.reply_text(off)
    else:
        await message.reply_text("**No ongoing process!**")
        return


#Tagall
@client.on_message(
    filters.command(["kuku","pain"], prefixes=["/", ".", "?", "-", "", "!"])
    & filters.group
)
async def tag_all_users(_, message):
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ["administrator", "creator"]:
        return await message.reply_text("**Only admins can use this command!**")
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text("**Reply to a message or give some text to tag all!**")
        return
    text = random.choice(TAGMES)
    SPAM_CHATS.append(message.chat.id)
    usernum = 0
    usertxt = ""
    members = await client.get_chat_members(message.chat.id)
    member_iter = iter(members)
    while message.chat.id in SPAM_CHATS:
        try:
            m = next(member_iter)
            usernum += 1
            usertxt += f" [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 1:
                if replied:
                    await replied.reply_text(usertxt)
                else:
                    await client.send_message(message.chat.id, f'{random.choice(TAGMES)}\n{usertxt}')
                await asyncio.sleep(15)
                usernum = 0
                usertxt = ""
        except StopIteration:
            break

    try:
        SPAM_CHATS.remove(message.chat.id)
    except Exception:
        pass

client.run()
