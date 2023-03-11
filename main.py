from pyrogram.errors import FloodWait
from configparser import ConfigParser
from pyrogram import Client, filters
from time import sleep
import settings
import random
import sys


config = ConfigParser()
config.read("config.ini")


language = config["USER"]["language"]
spam = False

delay = 0.25
if config["USER"]["language"] == "":
    language = "EN"
else:
    language = config["USER"]["language"]
if len(sys.argv) == 2:
    var = sys.argv[1]

    if var == "del":
        settings.Delete_session()
        print(config[language]["del_end"])
    elif var == "language":
        settings.set_language()
        print(config[language]["set_languages_end"])
    elif var == "-h":
        text = ""
        for i in config[language]["help_console"]:

            if i == "Ø":
                text += "\n"
            else:
                text += i

        print(text)
    else:
        print(config[language]["wtf"])
else:
    if (
        config["USER"]["api_hash"] == ""
        or config["USER"]["api_id"] == ""
        or language == ""
    ):
        settings.set_basic_settings()
        config = ConfigParser()
        config.read("config.ini")
    language = language
    app = Client(
        "my_account",
        api_id=config["USER"]["api_id"],
        api_hash=config["USER"]["api_hash"],
    )
    print(config[language]["start_app"])

    @app.on_message(filters.command("help", prefixes=".") & filters.me)
    def help(_, msg):

        text = ""
        for i in config[language]["help_text"]:
            if i == "Ø":
                text += "\n"
            else:
                text += i
        app.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=text)

    @app.on_message(filters.command("stop", prefixes=".") & filters.me)
    async def stop(_, msg):
        global spam
        await msg.delete()
        spam = False

    @app.on_message(filters.command("spam", prefixes=".") & filters.me)
    async def spam(_, msg):
        global spam
        orig_text = str(msg.text.split(".spam", maxsplit=1)[1])
        orig_text_list = orig_text.split()
        text = str(msg.text.split(orig_text_list[0], maxsplit=1)[1])

        spam = True
        loop = orig_text_list[0]
        if loop.isdigit() == True:
            await msg.delete()
            if int(loop) == 0:
                while spam:
                    try:
                        await msg.reply_text(text)
                        sleep(delay)
                    except FloodWait as e:
                        sleep(e.x)
            for i in range(int(loop)):
                if spam == True:
                    try:
                        await msg.reply_text(text)
                        sleep(delay)
                    except FloodWait as e:
                        sleep(e.x)

    @app.on_message(filters.command("spam_list", prefixes=".") & filters.me)
    async def spam_list(_, msg):
        global spam
        orig_text = str(msg.text.split(".spam", maxsplit=1)[1])
        orig_text_list = orig_text.split()
        text = str(msg.text.split(orig_text_list[0], maxsplit=1)[1])

        msg_list = []
        for i in text.split("|"):
            if i != "" and i != " ":
                msg_list.append(i)
        spam = True
        loop = orig_text_list[0]
        if loop.isdigit() == True:
            await msg.delete()
            if int(loop[0]) == 0:
                while spam:
                    for message in msg_list:
                        await msg.reply_text(message)
                        sleep(delay)
            for i in range(int(loop[0])):
                if spam == True:
                    for message in msg_list:
                        try:
                            await msg.reply_text(message)
                            sleep(delay)
                        except FloodWait as e:
                            sleep(e.x)

    @app.on_message(filters.command("decryption", prefixes=".") & filters.me)
    def decryption(_, msg):
        orig_text = msg.text.split(".decryption", maxsplit=1)[1]

        message = ""
        symbols = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о","п",
                   "р", "с","т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я", "А", "Б", "В", "Г", "Ґ", "Д","Е",
                   "Є", "Ж","З", "И","І", "Ї", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц",
                   "Ч", "Ш", "Щ", "Ь","Ю", "Я","A", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                   "P", "Q", "R", "S", "T", "U","V", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                   "j", "k", "l", "m", "n", "o", "p", "q","r", "s","t", "u", "v", "w", "x", "y", "z", "1", "2", "3",
                   "4", "5", "6", "7", "8", "9", "0", "!","\"", "#","$", "%","&", "\'", "(", ")", "*", "+", ",","-",
                   ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_","`","{", "|", "}", "~", "\\"
                   ]

        for symbol_orig in orig_text:
            loop = random.randint(5, 10)
            symbols_old = ""
            for i in range(loop):

                symbol_new = random.choice(symbols)

                if not symbol_new == symbols_old and not symbol_new == symbol_orig:
                    try:
                        app.edit_message_text(
                            chat_id=msg.chat.id,
                            message_id=msg.id,
                            text=f"{message}{symbol_new}",
                        )

                        symbols_old = symbol_new
                        sleep(0.5)
                    except FloodWait as e:
                        sleep(e.x)

            message += symbol_orig
            sleep(0.10)
        app.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=f"{message}")

    @app.on_message(filters.command("type", prefixes=".") & filters.me)
    def type(_, msg):
        orig_text = msg.text.split(".type ", maxsplit=1)[1]
        text = orig_text
        tbp = ""
        typing_symbol = "▒"

        while tbp != orig_text:
            try:
                msg.edit(tbp + typing_symbol)
                sleep(0.05)  # 50 ms

                tbp = tbp + text[0]
                text = text[1:]

                msg.edit(tbp)
                sleep(0.05)

            except FloodWait as e:
                sleep(e.x)

    app.run()
