import re
from main.client import bot 
from pyrogram import filters 
from pyrogram.type import Message

STATS = []

@bot.on_message(filters.command(pattern="stats" & filters.all))
async def stats(msg: Message):
        stats = "📊𝙂𝙍𝙊𝙐𝙋 𝙎𝙏𝘼𝙏𝙎:\n" + "\n".join([mod.__stats__() for mod in STATS])
        result = re.sub(r"(\d+)", r"\1", stats)
        await msg.send_message(msg.chat.id, result)
