import os
from typing import List
import telebot

bot = telebot.TeleBot("1936340534:AAHw-G8p5QyDzplONwr2qqD89dK92Da7BVI")

PM_START_TEXT = """
๐๐๐ก๐ก๐ค ๐ฉ๐๐๐ง๐, ๐'๐ข [VndGroup](t.me/vndgroupbotchannle) ๐ฅ
๐'๐ข ๐ ๐๐ค๐ฌ๐๐ง๐๐ช๐ก ๐๐ง๐ค๐ช๐ฅ ๐ข๐๐ฃ๐๐๐๐ง ๐๐ค๐ฉ ๐๐๐ฉ๐ ๐พ๐ค๐ค๐ก ๐๐ค๐๐ช๐ก๐๐จ. ๐๐๐๐ ๐๐ฎ [Team VndGroup](t.me/vndgroupbotchannle)
๐๐๐ฉ /help ๐ฉ๐ค ๐๐๐ฃ๐ ๐ข๐ฎ ๐ก๐๐จ๐ฉ ๐ค๐ ๐๐ซ๐๐๐ก๐๐๐ก๐ ๐๐ค๐ข๐ข๐๐ฃ๐๐จ ๐น
 
"""

buttons = [
    [
        InlineKeyboardButton(text="๐แดแดแดแดแดแด๊ฑ แดสแดษดษดแดส", url="https://t.me/vndgroupbotchannle"),
        InlineKeyboardButton(text="๐ฒ ๊ฑแดแดแดแดสแด ษขสแดแดแด", url="https://t.me/vndgroupbotchannle"),
    ],
    [
        InlineKeyboardButton(text="๐ owner", url="https://t.me/Venuja_Sadew"),
        InlineKeyboardButton(text="โ สแดสแด", url="https://t.me/vndgroupbotchannle"),
    ],
    [
        InlineKeyboardButton(
            text="โ แดแดแด VndGroup Bot แดแด สแดแดส ษขสแดแดแด โ", url="t.me/TheAnkiVectorbot?startgroup=true"
        ),
    ],
]