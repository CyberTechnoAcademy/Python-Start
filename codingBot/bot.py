import telebot
from telebot import types

bot = telebot.TeleBot('5201985112:AAGEs2e-BTsm8fQTr0YgeIXAb-o9iXsnV5U')

@bot.message_handler(commands=['start'])
def start(message):
	clava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

	games = types.KeyboardButton('Создание игр 🎮')
	mobie_app = types.KeyboardButton('Мобильные приложения📱')
	computer_app = types.KeyboardButton('Софт для компьютеров 💻')
	artificial_intelligence = types.KeyboardButton('Искусственный интеллект 🤖')
	web = types.KeyboardButton('Веб-разработка 🌐')
	data = types.KeyboardButton('Обработка данных 📊')

	clava.add(games, mobie_app, computer_app, artificial_intelligence, web, data)

	send_mess = f"<b>Привет 👋</b>" + \
	"\nКакое направление тебя интересует?"
	
	bot.send_message(message.chat.id, send_mess, 
	parse_mode='html', reply_markup=clava)

@bot.message_handler(content_types=['text'])
def mess(message):
	
	if message.text == "Создание игр 🎮":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		mobile = types.KeyboardButton('Под мобильные телефоны 📱')
		computer = types.KeyboardButton('Компьютеры и консоли 🖥')
		vr = types.KeyboardButton('Виртуальная реальность 👓')
		web = types.KeyboardButton('Веб-игра 🌐')
		back = types.KeyboardButton("Назад 🔙")
		markup.add(mobile, computer, vr, web, back)

		final_message = "Отлично, геймдев крутая тема.\nПод что хочется разрабатывать?"
		bot.send_message(message.chat.id, final_message, 
		parse_mode='html', reply_markup=markup)

	elif message.text == "Под мобильные телефоны 📱":
		markup = types.InlineKeyboardMarkup()

		unity = types.InlineKeyboardButton(
			"Посмотреть курсы по Unity", 
			url="https://itproger.com/tag/unity"
		)
		markup.add(unity)

		final_message = "Для разработки игр под мобильные\
		устройства зачастую используется игровой движок <b>Unity</b>"

		bot.send_photo(message.chat.id, photo=open("./codingBot/images/unity.png", 'rb'))
		bot.send_message(message.chat.id, final_message, parse_mode='html', 
		reply_markup=markup)
		

	elif message.text == 'Назад 🔙':
		send_mess = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"
		clava = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		
		games = types.KeyboardButton('Создание игр 🎮')
		mobie_app = types.KeyboardButton('Мобильные приложения📱')
		computer_app = types.KeyboardButton('Софт для компьютеров 💻')
		artificial_intelligence = types.KeyboardButton('Искуственный интелект 🤖')
		web = types.KeyboardButton('Веб-разработка 🌐')
		data = types.KeyboardButton('Обработка данных 📊')

		clava.add(games, mobie_app, computer_app, artificial_intelligence, web, data)
		bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=clava)

bot.polling(none_stop=True)