import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
AM = getenv("AM","5360305806")
OWNER = getenv("OWNER","Sanam_King")
BOT_TOKEN = getenv("BOT_TOKEN","5978355046:AAGCmUjoFrOBubx_XLioRJQ8KFCzm5hbZco")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ShizukaMusic:IKbpOwpgPA3C3NfK@shizukamusic.h0d0rs6.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9000"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001840241140"))
OWNER_ID = int(getenv("OWNER_ID", "5360305806"))
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "30"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","shizukamusicbbb")
HEROKU_API_KEY = getenv("HEROKU_API_KEY","601f56a4-dac8-4f9e-96af-8996ddfff3e2")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiMod/ShizukaMusic",
)
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+hRDHHhgdtT5lMTFl")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", "BQBrNQAyOp5reErmjtqbqObXDMrIa_dePfIMmkOmpWHeufIEMYjazwKUXZcG9t_YmRCeM31dmIwYcQlb-w8otF4mVWafRWCHZ7RHtFlhdi1q3L--iT5TsJkLHURdRgXiqV_47QPTZBug8ro_rF6b8hOjaky918WZHWqTEisjAZP8oK-IGqjxTcLSgARGl-SVNShSdE3q40Gl3WxndNfMpbcJsQbzElmUQLuSWHuuOS0nlnugacSvHmrCAHpPkXDp9NMsHLn38r85gOSYERQ7mU7xhRGXESl-z3IcNBJN5ZTcY8PDw_jUoDVAASfgoXoFKJygQhSRkCSamP-kOUVFBYg_AAAAAY-_678A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", "https://graph.org/file/d5da08b65b054e7183ae9.jpg", "https://graph.org/file/941558bfd46ee7f4c805b.jpg", "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", "https://graph.org/file/2311d35739ca433f0b1c9.jpg", "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", "https://graph.org/file/13e35118f9db15f85d085.jpg"]
PING_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", "https://graph.org/file/d5da08b65b054e7183ae9.jpg", "https://graph.org/file/941558bfd46ee7f4c805b.jpg", "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", "https://graph.org/file/2311d35739ca433f0b1c9.jpg", "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", "https://graph.org/file/13e35118f9db15f85d085.jpg"]
STATS_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", "https://graph.org/file/d5da08b65b054e7183ae9.jpg", "https://graph.org/file/941558bfd46ee7f4c805b.jpg", "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", "https://graph.org/file/2311d35739ca433f0b1c9.jpg", "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", "https://graph.org/file/13e35118f9db15f85d085.jpg"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
