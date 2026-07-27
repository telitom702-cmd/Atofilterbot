import re
from os import environ

def bool_environ(var): 
    if isinstance(var, bool):
        return var
    return str(var).lower() in ("true", "1", "t", "y", "yes")

id_pattern = re.compile(r'^-?\d+$')

SESSION = 'TechVJBot'
API_ID = 24776633
API_HASH = '57b1f632044b4e718f5dce004a988d69'
BOT_TOKEN = "8998188048:AAFLvJ7xkydWpTPlskOIM4tiCwmVGPAbOZA"

PICS = 'https://graph.org/file/ce1723991756e48c35aa1.jpg'.split()

ADMINS = [8248792819]
AUTH_USERS = []

LOG_CHANNEL = -1003084490680  # Note: Added minus for channel ID
CHANNELS = []

REQUEST_TO_JOIN_MODE = False
TRY_AGAIN_BTN = False

AUTH_CHANNEL = None
REQST_CHANNEL = None
INDEX_REQ_CHANNEL = LOG_CHANNEL
SUPPORT_CHAT_ID = None

FILE_STORE_CHANNEL = [-1003036018855] # Note: Added minus for channel ID
DELETE_CHANNELS = []

DATABASE_URI = "mongodb+srv://mongodbpy_db_user:pPgtRKyHsm8GvJF2@cluster0.u2ft5ps.mongodb.net/?appName=Cluster0"
DATABASE_NAME = "techvjclonefilterbot"
COLLECTION_NAME = 'vjcollection'

MULTIPLE_DATABASE = False
O_DB_URI = ""
F_DB_URI = "" 
S_DB_URI = ""

PREMIUM_AND_REFERAL_MODE = True
REFERAL_COUNT = 20
REFERAL_PREMEIUM_TIME = '1month'
PAYMENT_QR = 'https://graph.org/file/ce1723991756e48c35aa1.jpg'
PAYMENT_TEXT = '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 30ʀs - 1 ᴡᴇᴇᴋ\n- 50ʀs - 1 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n\n✨ ᴜᴘɪ ɪᴅ - <code>demo@okxyz</code></b>'

GRP_LNK = 'https://t.me/Tec_omar'
CHNL_LNK = 'https://t.me/Tec_omar'
SUPPORT_CHAT = 'Tec_omar' 
OWNER_LNK = 'https://t.me/Tec_omar'

AI_SPELL_CHECK = True
PM_SEARCH = True
BUTTON_MODE = True
MAX_BTN = True
IS_TUTORIAL = False
IMDB = False
AUTO_FFILTER = True
AUTO_DELETE = True
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True
NO_RESULTS_MSG = False
USE_CAPTION_FILTER = True

CACHE_TIME = 1800
MAX_B_TN = "5"
PORT = int(environ.get("PORT", 10000)) 
MSG_ALRT = 'Hello My Dear Friends ❤️'
CUSTOM_FILE_CAPTION = "<b>{file_name}</b>\n\n@Tec_omar"
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION
IMDB_TEMPLATE = "<b>{title}</b>\n\n{plot}"
MAX_LIST_ELM = None

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "ban"]
SEASONS = ["season 1", "season 2", "auto", "ban", "season 3", "season 4", "season 5", "season 6", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E10"]
QUALITIES = ["360p", "480p", "auto", "ban", "720p", "1080p", "1440p", "2160p"]
YEARS = ["2000", "2024", "2025"]

STREAM_MODE = True
MULTI_CLIENT = False
SLEEP_THRESHOLD = 60
PING_INTERVAL = 1200
ON_HEROKU = False
URL = "https://your-render-app-name.onrender.com/"

RENAME_MODE = False
AUTO_APPROVE_MODE = False

REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI
