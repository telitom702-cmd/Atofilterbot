import asyncio
from aiohttp import web
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import API_ID, API_HASH, BOT_TOKEN, SESSION, PICS, ADMINS, GRP_LNK, CHNL_LNK, OWNER_LNK, PORT
from utils.temp import temp

# Initialize Bot
app = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ==========================================
# LOADING ALL PLUGINS (CRITICAL FEATURE)
# ==========================================
print("Loading Plugins...")
async def load_plugins():
    # এই কোডটি plugins ফোল্ডারের ভেতরের সব .py ফাইল (auto_filter, index) বটে অটোমেটিক লোড করবে
    import importlib
    import os
    from pathlib import Path
    
    plugin_dir = Path("plugins")
    for file in plugin_dir.glob("*.py"):
        if file.name.startswith("__"):
            continue
        module = importlib.import_module(f"plugins.{file.stem}")
        print(f"Loaded Plugin: {file.stem}")

# ==========================================
# START COMMAND
# ==========================================
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

# ==========================================
# WEB SERVER SETUP FOR RENDER
# ==========================================
async def web_server():
    web_app = web.Application(client_max_size=30000000)
    
    async def health_check(request):
        return web.Response(text="Bot is running perfectly!")
        
    web_app.add_routes([web.get('/', health_check)])
    return web_app

# ==========================================
# MAIN FUNCTION (RUNNING EVERYTHING)
# ==========================================
async def main():
    # 1. Load all plugin files from 'plugins' folder
    await load_plugins()
    
    # 2. Start the Web Server for Render Port Binding
    server = await web_server()
    runner = web.AppRunner(server)
    await runner.setup()
    
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"Web Server started on Port {PORT}")

    # 3. Start the Pyrogram Bot
    await app.start()
    print("Bot is started and all features are active!")
    
    # 4. Keep the bot running until manually stopped
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
