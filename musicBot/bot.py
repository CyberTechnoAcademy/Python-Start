import telebot
from telebot import types

playlists = {}
songs = {"moonlight": "musicBot\music\moonlight.mp3", "lean on": "musicBot\music\Lean on.mp3"}

bot = telebot.TeleBot('5155080476:AAGUePP9g_H9TDacLQ1FCxrkZwFXVn5-8cs')

@bot.message_handler(commands=['start'])
def start(message):

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

  playlist = types.KeyboardButton('Мой плейлист 📻')
  popular = types.KeyboardButton('Популярное 🔥')
  genres = types.KeyboardButton('Жанры 🎧')
  search = types.KeyboardButton('Поиск 🔎')

  markup.add(playlist, popular, genres, search)

  send_mess = f"<b>Привет!</b>\nКакое направление тебя интересует? 🔊"

  bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
  if message.text == "Жанры 🎧":
    markup = types.InlineKeyboardMarkup(row_width=1)

    rap = types.InlineKeyboardButton('Рэп', callback_data='rap')
    pop = types.InlineKeyboardButton('Поп-музыка', callback_data='pop')
    jazz = types.InlineKeyboardButton('Рок', callback_data='jaz')
    rock = types.InlineKeyboardButton('Шансон', callback_data='rock')

    send_message = "Что предпочитаешь больше? 🤔"
    markup.add(rap, pop, jazz, rock)

    bot.send_message(message.chat.id, send_message, reply_markup=markup)

  elif message.text == "Мой плейлист 📻":
    
    send_message = 'Введите название плейлиста: '

    msg =  bot.send_message(message.chat.id, send_message, parse_mode='html')

    bot.register_next_step_handler(msg, playlist)
  
  elif message.text == "Поиск 🔎":
    
    send_message = 'Введите название трека: '
    
    msg = bot.send_message(message.chat.id, send_message)

    bot.register_next_step_handler(msg, search_songs)
    
  elif message.text in playlists.keys():
    
    markup = types.InlineKeyboardMarkup()
    track_counts = len(playlists[message.text])

    for c in range(track_counts):  
      track = playlists[message.text][c]
      track_button = types.InlineKeyboardButton(track, callback_data=track)
      markup.add(track_button)

    bot.send_message(message.chat.id, f'Плейлист "{playlist_name}" ',
    reply_markup=markup)

def playlist(message): 
  global playlist_name 

  playlist_name = message.text

  markup = types.InlineKeyboardMarkup(row_width=2)

  lean_on = types.InlineKeyboardButton('Lean on', callback_data='lean_on')
  the_lazy_song = types.InlineKeyboardButton('The lazy song', callback_data='the_lazy_song')
  remember_the_name = types.InlineKeyboardButton('Remember The Name', callback_data='Remember The Name')
  smooth_criminal = types.InlineKeyboardButton('Smooth Criminal', callback_data='Smooth Criminal')
  enemy = types.InlineKeyboardButton('Enemy', callback_data='Enemy')
  goosebumps = types.InlineKeyboardButton('Goosebumps', callback_data='Goosebumps')

  markup.add(lean_on, the_lazy_song, remember_the_name, smooth_criminal, enemy, goosebumps )
  bot.send_message(message.chat.id, f'Плейлист "{playlist_name}". Выберите треки: ', reply_markup=markup)

def search_songs(message):
  if message.text in songs.keys():
    bot.send_audio(message.chat.id, audio=open(songs[message.text], 'rb'))
  else: 
    bot.send_message(message.chat.id, 'Данный трек отсутсвует в базе данных')

@bot.callback_query_handler(func = lambda callback: callback.data == 'lean_on')
def lean_on(callback: types.CallbackQuery):
  
  if playlist_name not in playlists.keys():
    playlists.update({playlist_name: []})
    playlists[playlist_name].append('Lean on')
  else: 
    playlists[playlist_name].append('Lean on')

@bot.callback_query_handler(func=lambda callback: callback.data == 'the_lazy_song')
def the_lazy_song(callback: types.CallbackQuery):
  if playlist_name not in playlists.keys():
    playlists.update({playlist_name: []})
    playlists[playlist_name].append('The lazy song')
  else:
    playlists[playlist_name].append('The lazy song')

@bot.callback_query_handler(func = lambda callback: callback.data == 'rap')
def rap(callback: types.CallbackQuery):

  markup = types.InlineKeyboardMarkup(row_width=1)

  in_da_club = types.InlineKeyboardButton('In Da Club', callback_data="In Da Club")
  till_i_collapse = types.InlineKeyboardButton('Till I Collapse', callback_data='Till')
  still_dre = types.InlineKeyboardButton('Still D.R.E.', callback_data='Still D.R.E')
  moonlight = types.InlineKeyboardButton('Moonlight', callback_data='moonlight')

  markup.add(in_da_club, till_i_collapse, still_dre, moonlight)

  bot.send_message(callback.from_user.id, 'Наслаждайся 🎵', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'moonlight')
def moonlight(callback: types.CallbackQuery):

 bot.send_audio(callback.from_user.id, audio=open('musicBot\music\moonlight.mp3','rb'))

@bot.callback_query_handler(func=lambda callback: callback.data == 'Lean on')
def moonlight(callback: types.CallbackQuery):
  bot.send_audio(callback.from_user.id, audio=open('musicBot\music\Lean on.mp3', 
  'rb'))

@bot.callback_query_handler(func=lambda callback: callback.data == 'The lazy song')
def moonlight(callback: types.CallbackQuery):
  
  bot.send_audio(callback.from_user.id, audio=open('musicBot\music\The lazy song.mp3', 
  'rb'))

bot.polling(none_stop=True)