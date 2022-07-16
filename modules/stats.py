import re
from main.client import bot 
from pyrogram import filters 
from pyrogram.types import Message
DEV = [
1366616835 # @Alone_loverboy
]
STATS = []

@bot.on_message(filters.command(pattern="stats"))
async def stats(msg: Message):
        if msg.sender.id==DEV:
          stats = "📊𝐆𝐑𝐎𝐔𝐏 𝐒𝐓𝐀𝐓𝐒 ➮:\n" + "\n".join([mod.__stats__() for mod in STATS])
          result = re.sub(r"(\d+)", r"\1", stats)
          await msg.send_message(msg.chat.id, result)
        else:
          await bot.send_message(msg.chat.id, "Stupid\n\nYou don't have access!")
