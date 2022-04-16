import telebot
from os import listdir, remove, makedirs, startfile, system;from random import choice;from telebot import types
bot = telebot.TeleBot('5243812043:AAEJCREukofJVGXrffEc5GpC0cGZREcdpD4')

Max_Files_For_User = 6
Black_Listed_Librarys = [' os', ',os', 'base64', 'input',
                         'bot.py', 'base32', 'marshal',
                         'selenium', 'webbrowser']


@bot.message_handler(commands=['start'])
def home(message):
    try:
        with open('data.txt', 'r') as data_file:
            df = data_file.readlines()
            data_file.close()
            if str(message.chat.id) not in df:
                with open('data.txt', 'a') as data_file:
                    data_file.write(str(message.chat.id)+'\n')
                    data_file.close()

        key = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/harithTools')
        b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
        key.add(b1);key.add(b2)
        bot.send_video(message.chat.id, 'https://t.me/thuuu/9',
                       caption=f'*Welcome* To the best *Python* host bot\n**Currently version: V0.4**\nMade By: @HarithTools\n\n*Cmds*:\n/help ( *To get the help page* )\n/files ( *To get your files* )\n/lib ( *more info about libraries* )\n/get + Your file id ( *To get your file* )\n/pip + Library name ( *To install a Library* )\n/run + Your file Id ( *To run your bot* )',
                       parse_mode='markdown',
                       reply_markup=key)
    except:
        bot.send_message(message.chat.id, text="*Error while loading* 🚫\nPlease contact the coder: @HarithTools",
                         parse_mode='markdown')


@bot.message_handler(func=lambda m: True)
def get(message):
    msg = message.text
    try:
        if msg.startswith('/pip'):
            try:
                data = str(msg).split(' ')
                the_pip = data[1]

                if 'telebot' in the_pip or 'pyTelegramBotAPI' in the_pip or 'requests' in the_pip:
                    bot.send_message(message.chat.id, text="Installed by the developer ✅")
                else:
                    system(f"pip install {the_pip}")
                    bot.send_message(message.chat.id, text="Install success! ✅")

            except:
                bot.send_message(message.chat.id,
                                 text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start")

        elif msg.startswith('/run'):
            try:

                data = str(msg).split(' ')
                the_file_name = data[1]

                startfile(f"bots\{message.chat.id}\{the_file_name}.py")
                bot.send_message(message.chat.id, text="Your script is running! ✅")

            except:
                bot.send_message(message.chat.id,
                                 text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

        elif msg.startswith('/help'):
            try:

                key = types.InlineKeyboardMarkup()
                b1 = types.InlineKeyboardButton(text='Coder', url='https://t.me/HarithTools')
                b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
                key.add(b1)
                key.add(b2)

                bot.send_photo(message.chat.id, photo='https://t.me/thuuu/8',
                               caption="*Help Page* 📑\n1- Drag your python file to the bot\n2- Then the bot will give you *File ID*\n\n3- Then install your Librarys\n 🔍 using /pip + *library name*\n\n4- Run your bot\n 🔍 using /run + *File iD*\n\n*Contact*: @HarithTools",
                               parse_mode='markdown', reply_markup=key)

            except:
                bot.send_message(message.chat.id,
                                 text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start ")

        elif msg.startswith('/files'):
            try:

                key = types.InlineKeyboardMarkup()
                b1 = types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/HarithTools')
                b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
                key.add(b1)
                key.add(b2)

                files = listdir(f'bots/{message.chat.id}')
                lenfiles = len(files)
                msgfile = '''┌ Your Files\n'''
                for i in range(lenfiles):
                    msgfile += '├ ' + files[i].split('.')[0] + '\n'

                msgfile += '└ ' + f'ID: {message.chat.id}' + '\n'

                bot.send_message(message.chat.id, text=msgfile,
                                 parse_mode='markdown', reply_markup=key)

            except:
                bot.send_message(message.chat.id,
                                 text=f"Sorry you dont have files yet!")

        elif msg.startswith('/lib'):
            try:

                key = types.InlineKeyboardMarkup()
                b1 = types.InlineKeyboardButton(text='Channel 📢', url='https://t.me/Avira')
                b2 = types.InlineKeyboardButton(text='Source code </>', url='https://github.com/PluginX/Host-Bot/')
                key.add(b1)
                key.add(b2)

                Black_Listed_Librarys.reverse()
                msgfile = '''┌ *Not allowed*\n'''
                for i in Black_Listed_Librarys:
                    msgfile += '├ ' + i.title() + '\n'

                msgfile += '└ ' + f'ID: {message.chat.id}' + '\n'

                bot.send_message(message.chat.id, text=msgfile,
                                 parse_mode='markdown', reply_markup=key)

            except:
                bot.send_message(message.chat.id,
                                 text=f"Sorry you don't have files yet!")

        elif msg.startswith('/get'):
            try:

                data = str(msg).split(' ')
                the_file_name = data[1]
                with open(f'bots/{message.chat.id}/{the_file_name}.py', 'rb') as readbytes:
                    rdr = readbytes.read()
                readbytes.close()
                bot.send_document(message.chat.id, rdr, )

            except:
                bot.send_message(message.chat.id, text=f"Sorry you don't have that file!")

        else:
            bot.send_message(message.chat.id,
                             text=f"Sorry you leave something empty!\nOr you are missing some requires\nPlease try again /start")
    except:
        bot.send_message(message.chat.id,
                         text="*Error while* 🚫\nPlease contact the coder: @HarithTools",
                         parse_mode='markdown')


@bot.message_handler(content_types=['document'])
def save(message):
    chars, ran = 'abcdefghijklmnopqrstuvwxyz1234567890', 'a'
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    for i in range(32):
        ran += str(choice(chars))

    try:
        makedirs('bots/' + str(message.chat.id) + '/')
    except:
        pass
    with open('bots/' + str(message.chat.id) + '/' + ran + '.py', 'wb') as new_file:
        new_file.write(downloaded_file)

    getlen = len(listdir('bots/' + str(message.chat.id) + '/'))
    if int(getlen) >= int(Max_Files_For_User + 1):
        bot.send_message(message.chat.id,
                         text=f'*You have upload {getlen} files\n You cant upload more* 🚫',
                         parse_mode='markdown')

        remove('bots/' + str(message.chat.id) + '/' + ran + '.py')
    else:
        try:
            black_lib, bol = '', False
            for i in Black_Listed_Librarys:
                search = str(downloaded_file).find(i)
                if search > 0:
                    bol = True
                    black_lib += i
                    break

            if bol:
                bot.reply_to(message, text=f'You cant use *{black_lib}* 🚫\nFile Removed! ', parse_mode='markdown')
                remove('bots/' + str(message.chat.id) + '/' + ran + '.py')
            else:
                bot.send_message(message.chat.id, text=f'*File upload success* ✅\n*Your File ID*:',
                                 parse_mode='markdown')
                bot.send_message(message.chat.id, text=f'```{ran}```', parse_mode='markdown')
        except:
            bot.send_message(message.chat.id,
                             text=f'*Error in file upload contact the coder* 🚫\nPlease try again later',
                             parse_mode='markdown')


bot.polling(True)
