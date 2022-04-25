from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
- مرحبـاً بـك عزيـزي {}

- فـي بـوت {}

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس تم انشـاء هـذا البـوت بواسطـة : @FLASH_MASR
    """

    # Home Button
    home_buttons = [        [InlineKeyboardButton("- بـدء إستخـراج كـود .", callback_data="generate")],        [InlineKeyboardButton(text="- رجوع .", callback_data="home")]    ]

    generate_button = [        [InlineKeyboardButton("- بـدء إستخـراج كـود .", callback_data="generate")]    ]

    # Rest Buttons
    buttons = [        [InlineKeyboardButton("- بـدء إستخـراج كـود .", callback_data="generate")],        [InlineKeyboardButton("- مـطـور السـورس .", url="https://t.me/FLASH_MASR")],
        [            InlineKeyboardButton("- التعـليمـات ؟! .", callback_data="help"),            InlineKeyboardButton("- حـول البـوت .", callback_data="about")        ],]

    # Help Message
    HELP = """
** - اوامـر البــوت : **

/about - حـول البـوت
/help - التعليـمات
/start - ابـدأ 
/generate - بـدء إستخـراج جلسـه جديـده
/cancel - الغـاء
/restart - اعـادة الاستخـراج
"""

    # About Message
    ABOUT = """
**- حـول البـوت .** 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس جيبثون
- مـطـور السـورس : [—͟͟͞͞✯ ᏙᎥᎡႮՏ ┋✘🏴󠁧󠁢󠁥󠁮󠁧󠁿!](https://t.me/FLASH_MASR)

- المطور : @FLASH_MASR .

- لغـة البـوت : بـايثـون .
    """
