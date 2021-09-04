import os
from typing import List
import telebot

bot = telebot.TeleBot("1936340534:AAHw-G8p5QyDzplONwr2qqD89dK92Da7BVI")

PM_START_TEXT = """
𝙃𝙚𝙡𝙡𝙤 𝙩𝙝𝙚𝙧𝙚, 𝙄'𝙢 [VndGroup](t.me/vndgroupbotchannle) 🔥
𝙄'𝙢 𝙖 𝙋𝙤𝙬𝙚𝙧𝙛𝙪𝙡 𝙜𝙧𝙤𝙪𝙥 𝙢𝙖𝙣𝙖𝙜𝙚𝙧 𝙗𝙤𝙩 𝙒𝙞𝙩𝙝 𝘾𝙤𝙤𝙡 𝙈𝙤𝙙𝙪𝙡𝙚𝙨. 𝙈𝙖𝙙𝙚 𝙗𝙮 [Team VndGroup](t.me/vndgroupbotchannle)
𝙃𝙞𝙩 /help 𝙩𝙤 𝙛𝙞𝙣𝙙 𝙢𝙮 𝙡𝙞𝙨𝙩 𝙤𝙛 𝙖𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🕹
 
"""

buttons = [
    [
        InlineKeyboardButton(text="📌ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/vndgroupbotchannle"),
        InlineKeyboardButton(text="🖲 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/vndgroupbotchannle"),
    ],
    [
        InlineKeyboardButton(text="📜 owner", url="https://t.me/Venuja_Sadew"),
        InlineKeyboardButton(text="❔ ʜᴇʟᴘ", url="https://t.me/vndgroupbotchannle"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ VndGroup Bot ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="t.me/TheAnkiVectorbot?startgroup=true"
        ),
    ],
]