import asyncio
from datetime import datetime
from pyrogram import filters
from main.client import asst
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@asst.on_message(filters.command("start") & filters.private)
async def sstart(_,message : Message):
    await message.reply_photo(
    photo=f"https://te.legra.ph/file/900d41c5f02171fd21c9d.jpg",
    caption=f"""**ᴀ ᴡᴀʀᴍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀʟᴇxᴜs !! ɪ'ᴍ ʏᴏᴜʀ ᴀᴅᴠᴀɴᴄᴇ ɢʀᴏᴜᴘ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ\n\nI am very fast and relaible bot with advanced features!!!\nCreated by python3 and Pyrogram!\n\n

    ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ➪ [Alone_loverboy](https://t.me/Alone_loverBoy)\n\n[Nobita](https://t.me/nobitadev)

   ☺️ ᴋᴇᴇᴘ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ Aʟᴡᴀʏs ☺️ **""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♢🇦 🇩 🇩   🇲 🇪♢", url=f"https://t.me/alexusMusic_Bot?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "♢🇸 🇺 🇵 🇵 🇴 🇷 🇹♢", url=f"https://t.me/TeamAlexus")
                ]

            ]
         ),
     )
