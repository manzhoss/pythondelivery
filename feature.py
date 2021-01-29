import telebot
import sqlite3 as sq
from telebot import types

bot = telebot.TeleBot('1546752822:AAGK-9oiHqXlbZroKP8ydLKm4g-9xIf0qnA')

with sq.connect("classic.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        t_id INTEGER PRIMARY KEY,
        name TEXT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS details (
        t_id INTEGER PRIMARY KEY,
        dog TEXT,
        bell TEXT,
        door TEXT,
        baby TEXT
    )""")

# keyboards
mainKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mainACCEPT = types.KeyboardButton(text='Замовити')
mainDECS = types.KeyboardButton(text='Додати деталі до замовлення')
mainKeyboard.add(mainACCEPT, mainDECS)

detailsKeyboard = types.InlineKeyboardMarkup(row_width=2)
detailsA_DOG = types.InlineKeyboardButton(callback_data='a_dog', text='🐶')
detailsB_BELL = types.InlineKeyboardButton(callback_data='b_bell', text='🔕')
detailsB_PHONE = types.InlineKeyboardButton(callback_data='b_phone', text="🔐")
detailsBABY = types.InlineKeyboardButton(callback_data='baby', text="🚼")
detailsKeyboard.add(detailsA_DOG, detailsB_BELL, detailsB_PHONE, detailsBABY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello', reply_markup=mainKeyboard)
    try:
        with sq.connect("classic.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO details(t_id, dog, bell, door, baby) VALUES({message.chat.id}, '❌', '❌', '❌', '❌')")
    except:
        pass

@bot.message_handler(regexp='Додати деталі до замовлення')
def desc(message):
    with sq.connect("classic.db") as con:
        cur = con.cursor()
        dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {message.chat.id}")
        dog = cur.fetchone()[0]
        bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {message.chat.id}")
        bell = cur.fetchone()[0]
        door = cur.execute(f"SELECT door FROM details WHERE t_id = {message.chat.id}")
        door = cur.fetchone()[0]
        baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {message.chat.id}")
        baby = cur.fetchone()[0]
    bot.send_message(message.chat.id, f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼", reply_markup=detailsKeyboard)

@bot.callback_query_handler(func=lambda call: True)
def check(call):
    if call.data == 'a_dog':
        with sq.connect("classic.db") as con:
            cur = con.cursor()
            dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
            dog = cur.fetchone()[0]
            if dog == '❌':
                cur.execute(f"UPDATE details SET dog = '✅' WHERE t_id = {call.message.chat.id}")
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼", reply_markup=detailsKeyboard)
            elif dog == '✅':
                cur.execute(f"UPDATE details SET dog = '❌' WHERE t_id = {call.message.chat.id}")
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼", reply_markup=detailsKeyboard)
    elif call.data == 'b_bell':
        with sq.connect("classic.db") as con:
            cur = con.cursor()
            bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
            bell = cur.fetchone()[0]
            if bell == '❌':
                cur.execute(f"UPDATE details SET bell = '✅' WHERE t_id = {call.message.chat.id}")
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼",reply_markup=detailsKeyboard)
            elif bell == '✅':
                cur.execute(f"UPDATE details SET bell = '❌' WHERE t_id = {call.message.chat.id}")
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼",reply_markup=detailsKeyboard)
    elif call.data == 'b_phone':
        with sq.connect("classic.db") as con:
            cur = con.cursor()
            door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
            door = cur.fetchone()[0]
            if door == '❌':
                cur.execute(f"UPDATE details SET door = '✅' WHERE t_id = {call.message.chat.id}")
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼",reply_markup=detailsKeyboard)
            elif door == '✅':
                cur.execute(f"UPDATE details SET door = '❌' WHERE t_id = {call.message.chat.id}")
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼",reply_markup=detailsKeyboard)
    elif call.data == 'baby':
        with sq.connect('classic.db') as con:
            cur = con.cursor()
            baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
            baby = cur.fetchone()[0]
            if baby == '❌':
                cur.execute(f"UPDATE details SET baby = '✅' WHERE t_id = {call.message.chat.id}")
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼",reply_markup=detailsKeyboard)
            elif baby == '✅':
                cur.execute(f"UPDATE details SET baby = '❌' WHERE t_id = {call.message.chat.id}")
                door = cur.execute(f"SELECT door FROM details WHERE t_id = {call.message.chat.id}")
                door = cur.fetchone()[0]
                bell = cur.execute(f"SELECT bell FROM details WHERE t_id = {call.message.chat.id}")
                bell = cur.fetchone()[0]
                dog = cur.execute(f"SELECT dog FROM details WHERE t_id = {call.message.chat.id}")
                dog = cur.fetchone()[0]
                baby = cur.execute(f"SELECT baby FROM details WHERE t_id = {call.message.chat.id}")
                baby = cur.fetchone()[0]
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Деталі до замовлення:\n\n{dog} У мене є собака 🐶\n{bell} Не дзвонити у двері 🔕\n{door} Під'їзд з домофоном 🔐\n{baby} У мене мала дитина 🚼",reply_markup=detailsKeyboard)

bot.infinity_polling(True)