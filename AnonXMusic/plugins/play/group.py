import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["《جروب السورس》"], ""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/67ee91eccf50bebd4db7d.jpg",
caption=f"""[جروب رغي شباب وبنات 🌺❤️‍🔥](https://t.me/UI_OS)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "جروب رغي شباب وبنات 🌺❤️‍🔥", url=f"https://t.me/UI_OS"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "مالك الجروب", url=f"https://t.me/UP_UO"),
                ],
            ]
        ),
    )
