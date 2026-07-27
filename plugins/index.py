import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from database import db
from config import CHANNELS, ADMINS, FILE_STORE_CHANNEL

# Manual Index Command for Admins in Private Chat (Bot DM)
@Client.on_message(filters.command("index") & filters.private & filters.user(ADMINS))
async def manual_index(bot: Client, message: Message):
    """
    Admins can use /index in bot DM to index a specific channel.
    Usage: /index -1001234567890 (Channel ID)
    If no channel ID is provided, it will index channels from config.
    """
    # Check if a channel ID is provided in the command
    if len(message.command) > 1:
        try:
            target_chat = int(message.command[1])
        except ValueError:
            await message.reply_text("❌ Invalid Channel ID! Please provide a valid numeric ID like `-1001234567890`.")
            return
    else:
        # If no ID provided, use channels from config
        target_channels = CHANNELS + FILE_STORE_CHANNEL
        if not target_channels:
            await message.reply_text("❌ No channels configured in `CHANNELS` or `FILE_STORE_CHANNEL` to index!")
            return
        
        await message.reply_text(f"🔍 Starting auto-index for configured channels...\nChannels: {len(target_channels)}")
        
        total_files = 0
        for chat_id in target_channels:
            status_msg = await message.reply_text(f"📂 Indexing Channel: `{chat_id}`...")
            count = 0
            
            try:
                # Search for documents and videos in the channel
                async for msg in bot.search_messages(chat_id=chat_id, filter="document"):
                    if msg.document or msg.video or msg.audio:
                        file_id = msg.document.file_id if msg.document else msg.video.file_id if msg.video else msg.audio.file_id
                        file_name = msg.document.file_name if msg.document and msg.document.file_name else "Unknown"
                        file_size = msg.document.file_size if msg.document else msg.video.file_size if msg.video else msg.audio.file_size
                        caption = msg.caption if msg.caption else file_name
                        
                        # Upsert: Update if exists, insert if new. No duplicate issues!
                        db.save_file(
                            file_id=file_id,
                            file_name=file_name,
                            file_size=file_size,
                            caption=caption,
                            chat_id=msg.chat.id,
                            message_id=msg.id
                        )
                        count += 1
                        
                await status_msg.edit(f"✅ Indexed `{count}` files from `{chat_id}`")
                total_files += count
            except Exception as e:
                await status_msg.edit(f"⚠️ Failed to index `{chat_id}`: {e}")
                
        await message.reply_text(f"🎉 **Indexing Completed!**\nTotal files indexed across all channels: `{total_files}`")
        return

    # Indexing a single specific channel provided by the admin
    status = await message.reply_text(f"🔍 Starting index for Channel: `{target_chat}`...\nThis may take a while depending on the number of files.")
    count = 0
    
    try:
        async for msg in bot.search_messages(chat_id=target_chat, filter="document"):
            if msg.document or msg.video or msg.audio:
                file_id = msg.document.file_id if msg.document else msg.video.file_id if msg.video else msg.audio.file_id
                file_name = msg.document.file_name if msg.document and msg.document.file_name else "Unknown"
                file_size = msg.document.file_size if msg.document else msg.video.file_size if msg.video else msg.audio.file_size
                caption = msg.caption if msg.caption else file_name
                
                # Upsert logic
                db.save_file(
                    file_id=file_id,
                    file_name=file_name,
                    file_size=file_size,
                    caption=caption,
                    chat_id=msg.chat.id,
                    message_id=msg.id
                )
                count += 1
                
            # Update status every 100 files so the user knows it's working
            if count % 100 == 0:
                await status.edit_text(f"🔍 Indexing... `{count}` files processed so far.")

        await status.edit_text(f"✅ **Indexing completed successfully!**\n\nTotal files indexed: `{count}`")
    except Exception as e:
        await status.edit_text(f"❌ Indexing failed for `{target_chat}`!\nError: {e}")


# Auto-index new files as they arrive in channels
@Client.on_message(filters.channel & ~filters.forwarded)
async def auto_index_files(bot: Client, message: Message):
    """Auto-index new files in the channel to database"""
    # Check if the message is from a monitored channel
    if message.chat.id in CHANNELS or message.chat.id in FILE_STORE_CHANNEL:
        if message.document or message.video or message.audio:
            file_id = message.document.file_id if message.document else message.video.file_id if message.video else message.audio.file_id
            file_name = message.document.file_name if message.document and message.document.file_name else "Unknown"
            file_size = message.document.file_size if message.document else message.video.file_size if message.video else message.audio.file_size
            caption = message.caption if message.caption else file_name
            
            # Save to database using Upsert (Will update if exists, insert if new)
            db.save_file(
                file_id=file_id,
                file_name=file_name,
                file_size=file_size,
                caption=caption,
                chat_id=message.chat.id,
                message_id=message.id
            )
