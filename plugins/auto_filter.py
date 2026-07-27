from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import db
from config import PICS, CACHE_TIME, BUTTON_MODE, ADMINS
from utils.temp import temp

@Client.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def auto_filter(bot, message):
    query = message.text
    files = db.get_search_results(query)
    
    if not files:
        await message.reply_text("❌ No results found!")
        return

    buttons = []
    for file in files:
        # Creating a simple link to the file store or direct link
        # Here we just use the message_id and chat_id to generate a link
        chat_id = file.get('chat_id')
        msg_id = file.get('message_id')
        
        btn_text = f"{file['file_name'][:50]} - {file.get('file_size', 0) / (1024*1024):.1f} MB"
        url = f"https://t.me/c/{str(chat_id)[4:]}/{msg_id}" if str(chat_id).startswith('-100') else f"https://t.me/c/{chat_id}/{msg_id}"
        
        buttons.append([InlineKeyboardButton(text=btn_text, url=url)])

    await message.reply_text(
        f"🔍 **Search Results for:** `{query}`",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
