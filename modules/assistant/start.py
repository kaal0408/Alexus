import asyncio
from datetime import datetime
from pyrogram import filters
from main.client import asst
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@asst.on_message(command("start") & filters.private)
async def sstart(_,message : Message):
    await message.reply_text(
    f""" **ᴀ ᴡᴀʀᴍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀʟᴇxᴜs !!
    ɪ'ᴍ ʏᴏᴜʀ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ɴᴏ ʟᴀɢ ɢʀᴏᴜᴘ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ
    ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ➪ [ᴅᴇᴠ](https://t.me/Alone_loverBoy) ᴀɴᴅ [ᴅᴇᴠ](https://t.me/nobitadev)** """,
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🇦 🇩 🇩  🇲 🇪", url=f"https://t.me/alexusMusic_Bot?startgroup=true")
                ]
            ]
       )