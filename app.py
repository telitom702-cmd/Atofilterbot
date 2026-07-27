import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import API_ID, API_HASH, BOT_TOKEN, SESSION, PICS, ADMINS, GRP_LNK, CHNL_LNK, OWNER_LNK
from utils.temp import temp

# Initialize Bot
app = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    buttons = [
        [InlineKeyboardButton("📢 Channel", url=CHNL_LNK), InlineKeyboardButton("💬 Group", url=GRP_LNK)],
        [InlineKeyboardButton("👤 Owner", url=OWNER_LNK)]
    ]
    await message.reply_photo(
        photo=PICS[0],
        caption="**Hello! I am a File Filter Bot.**\n\nSend me a movie name, and I will find it for you! 🎬",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

print("Bot is starting...")
app.run()
