

import asyncio

import os
import time
import requests
from config import START_IMG_URL,  MUSIC_BOT_NAME
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

@app.on_message(
    command(["م1"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم اوامر الفتح والقفل في بوت {MUSIC_BOT_NAME} ميوزك\n
**قفل / تعطيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه

**فتح / تفعيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه
لتنصيب بوت مشابه تواصل معي فالخاص @UP_UO 
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱", url=f"https://t.me/UI_XB"),                        
                 ],[
                InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
               ],
          ]
        ),
    )
