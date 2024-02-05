import sqlite3
from create_bot import dp, bot
from aiogram.utils.markdown import text, bold, italic
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def sql_start():
    global base, cur
    base = sqlite3.connect('Easy Learn #3\easy_learn.db')
    cur = base.cursor()
    if base: 
        print("Data base connected OK!")
    base.execute('''CREATE TABLE IF NOT EXISTS materials (img TEXT, 
    name TEXT PRIMARY KEY, description TEXT)''')
    base.commit()

def sql_read_testing():
    base = sqlite3.connect('Easy Learn\easy_learn.db')
    cur = base.cursor()

    data = cur.execute('SELECT * FROM testing').fetchall()
    return data

def sql_read_translate():
    base = sqlite3.connect('Easy Learn\easy_learn.db')
    cur = base.cursor()

    data = cur.execute('SELECT * FROM translate').fetchall()
    return data

async def sql_add_command(state):
    global base, cur
    async with state.proxy() as data: 
        cur.execute('INSERT INTO material VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        if len(ret[2])>600:
                await bot.send_photo(message.from_user.id, ret[0], 
                text(bold(ret[1]))+'\n\n'+ret[2][:600], parse_mode=ParseMode.MARKDOWN)
                for x in range(200, len(ret[2]), 1000):
                    await bot.send_message(message.from_user.id, ret[2][x:x+1000], parse_mode=ParseMode.MARKDOWN)
        else:
               await bot.send_photo(message.from_user.id, ret[0], 
                text(bold(ret[1]))+'\n\n'+ret[2], 
                parse_mode=ParseMode.MARKDOWN)