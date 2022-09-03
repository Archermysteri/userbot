from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
from time import sleep
import random
import sqlite3
import os
spam = False
with sqlite3.connect("database.db") as db:

    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS id(id INTEGER PRIMARY KEY,api_id TEXT,api_hash TEXT)""")

    cursor = db.cursor()


    cursor.execute(f"""SELECT api_id FROM id WHERE id = 1 """)
    data = cursor.fetchone()
    cursor.execute(f"""SELECT api_hash FROM id WHERE id = 1  """)
    data1 = cursor.fetchone()

    if data == None:


        id = [1,input('api_id:'),input('api_hash:')]
        app = Client(
            "my_account",
            api_id=id[1],
            api_hash=id[2]
        )
        cursor.execute("""INSERT INTO id VALUES(?, ?, ?);""", id)
    else:
        k = input("Натисніть Enter(якщо хочете знищити сесію то напишіть del):")
        if k == "del":
            os.remove("database.db")
            os.remove("my_account.session")
            print("Зайдіть в налаштування Telegram видаліть сесію")

        else:
            cursor.execute(f"""SELECT api_id FROM id WHERE id = 1""")
            data = str(cursor.fetchone())
            data = data.replace('\'','')
            data = data.replace( '(', '')
            data = data.replace(')', '')
            api_id = data.replace(',', '')

            cursor.execute(f"""SELECT api_hash FROM id WHERE id = 1""")
            data = str(cursor.fetchone())
            data = data.replace('\'', '')
            data = data.replace('(', '')
            data = data.replace(')', '')
            api_hash = data.replace(',', '')




            app = Client(
                "my_account",
                api_id=api_id,
                api_hash=api_hash
            )
            print("Напишіть в чаті Telegram .help")

            delay = 0.25
            @app.on_message(filters.command("help", prefixes=".") & filters.me)
            def help(_, msg):
                orig_text='.1000-7-Запускае Я Гуль\n.spam "а" "повідомлення" - спамить повідомленням "а" разів якщо "а" дорівнює 0, то нескінченно раз\n.spam_list "а" "|повідомленя1|повідомленя2|повідомленя3|" - спамить декілько повідомлення "а" разів якщо "а" дорівнює 0, то нескінченно раз\n.stop - зупиняє спам\n.decryption "повідомлення"- дешифрує повідомлення\n.type "повідомлення" - друкує повідомлення\n.hack_dupa "чия дупа"-зламує дупу'
                app.edit_message_text(
                    chat_id=msg.chat.id,
                    message_id=msg.id,
                    text=orig_text
                )

            @app.on_message(filters.command('1000-7', prefixes='.') & filters.me)
            async def gol(_, message):
                s = 0.01
                b = 1007
                await message.delete()
                await message.reply_text(f'Я..')
                time.sleep(2)
                await message.reply_text(f'Гуль')
                while not  b <7:
                    if b <= 700:
                        s = delay

                    a=b-7

                    await message.reply_text(f'{a}-7')
                    b=a
                    time.sleep(s)

            @app.on_message(filters.command('stop', prefixes='.') & filters.me)
            async def stop(_, message):
                global spam

                await message.delete()
                spam = False

            @app.on_message(filters.command('spam', prefixes='.') & filters.me)
            async def spam(_, message):
                global spam
                orig_text = str(message.text.split(".spam", maxsplit=1)[1])
                cmd = orig_text.split()
                orig_text = str(message.text.split(cmd[0], maxsplit=1)[1])

                spam = True
                a = cmd[0]
                if a.isdigit() == True:
                    await message.delete()
                    if int(cmd[0])==0:
                        while spam:
                            await message.reply_text(orig_text)
                            time.sleep(delay)
                    for i in range(int(cmd[0])):
                        if spam == True:
                            await message.reply_text(orig_text)
                            time.sleep(delay)

            @app.on_message(filters.command('spam_list', prefixes='.') & filters.me)
            async def spam_list(_, message):
                global spam
                orig_text = str(message.text.split(".spam_list", maxsplit=1)[1])
                cmd = orig_text.split()
                orig_text = str(message.text.split(cmd[0], maxsplit=1)[1])
                k= orig_text.split("|")
                orig_text_list=[]
                for i in k:
                    if i!='' and i!=" ":
                        orig_text_list.append(i)
                spam = True
                a = cmd[0]
                print(a)
                if a.isdigit() == True:
                    await message.delete()
                    if int(cmd[0])==0:
                        while spam:
                            for i in orig_text_list:
                                await message.reply_text(i)
                                time.sleep(delay)
                    for i in range(int(cmd[0])):
                        if spam == True:
                            for i in orig_text_list:
                                await message.reply_text(i)
                                time.sleep(delay)


            @app.on_message(filters.command("decryption", prefixes=".") & filters.me)
            def decryption(_, msg):

                orig_text = msg.text.split(".decryption", maxsplit=1)[1]

                mesage =''
                A = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                     'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И',
                     'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я',
                     'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                     'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '"', '#', '$', '%',
                     '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
                     '{', '|', '}', '~', '\\']

                for ii in orig_text:
                    c = random.randint(5,10)
                    a_old=''
                    for i in range(c):



                        a_nue =random.choice(A)

                        if not a_nue == a_old and not a_nue == ii :

                            app.edit_message_text(
                                chat_id=msg.chat.id,
                                message_id=msg.id,
                                text=f'{mesage}{a_nue}'
                            )
                            a_old = a_nue
                        time.sleep(0.16)


                    mesage += ii
                    time.sleep(0.16)
                app.edit_message_text(
                    chat_id=msg.chat.id,
                    message_id=msg.id,
                    text=f'{mesage}'
                )




            @app.on_message(filters.command("type", prefixes=".") & filters.me)
            def type(_, msg):
                orig_text = msg.text.split(".type ", maxsplit=1)[1]
                text = orig_text
                tbp = ""
                typing_symbol = "▒"

                while (tbp != orig_text):
                    try:
                        msg.edit(tbp + typing_symbol)
                        sleep(0.05)  # 50 ms

                        tbp = tbp + text[0]
                        text = text[1:]

                        msg.edit(tbp)
                        sleep(0.05)

                    except FloodWait as e:
                        sleep(e.x)
            @app.on_message(filters.command("hack_dupa", prefixes=".") & filters.me)
            def hack_dupa(_, msg):
                orig_text = msg.text.split(".hack_dupa", maxsplit=1)[1]
                perc = 0

                while (perc < 100):
                    try:
                        text = f"‍💻‍Взлом Дупи  {orig_text} в в процесі ..." + str(perc) + "%"
                        msg.edit(text)

                        perc += random.randint(1, 3)
                        sleep(0.1)

                    except FloodWait as e:
                        sleep(e.x)

                msg.edit(f"🟢 Дупа {orig_text} успішно зламана!")
                sleep(3)

                msg.edit("🔞 Пошук порнухи")
                perc = 0

                while (perc < 100):
                    try:
                        text = "🔞 Пошук порнухи ..." + str(perc) + "%"
                        msg.edit(text)

                        perc += random.randint(1, 5)
                        sleep(0.15)

                    except FloodWait as e:
                        sleep(e.x)

                msg.edit("🔞 Знайдено дохуя гей порно серед них:\nГей порно з мавпами\nГей порно лунтик\nГей порно смешарики\nГей порно з ♂Dungeon Master♂")






            app.run()
