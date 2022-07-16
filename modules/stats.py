import re
from main.client import bot 
from pyrogram import filters 
from pyrogram.types import Message

STATS = []

@bot.on_message(filters.command(pattern="stats" & filters.all))
async def stats(msg: Message):
        stats = "📊𝐆𝐑𝐎𝐔𝐏 𝐒𝐓𝐀𝐓𝐒 ➮:\n" + "\n".join([mod.__stats__() for mod in STATS])
        result = re.sub(r"(\d+)", r"\1", stats)
        await msg.send_message(msg.chat.id, result)
