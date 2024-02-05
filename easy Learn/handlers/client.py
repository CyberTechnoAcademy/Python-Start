from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import basic_menu, test_ready, trainer_kb
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data_base import sqlite_db
import random

async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Привет! Что интересует? 🤔 ', 
        reply_markup=basic_menu)

async def text_message(message: types.Message):
        global rights
        if message.text == 'Тестирование 📝':
                await bot.send_message(message.from_user.id, 'Тест состоит из 4 вопросов. Готов?', reply_markup=test_ready)
        if message.text == 'Да':
                data = sqlite_db.sql_read_testing()
                await testing(data, message)
        if message.text == 'Нет'  or message.text == 'Назад ◀️':
                await bot.send_message(message.from_user.id, 'Обратно в главном меню 🔙', reply_markup=basic_menu)
        if message.text == 'Тренажер 🏋🏼':
                await bot.send_message(message.from_user.id, 'Пришло время улучшить навыки', reply_markup=trainer_kb)
        if message.text == 'Перевести предложение 💭':
                data = sqlite_db.sql_read_translate()
                await translate_send_first(data, message)

async def testing(data, message): 
        global questions, order_testing, rights, variants, right_answers
        rights = 0 
        order_testing = 0

        questions = []
        for entry in data:
                question = entry[0]
                questions.append(question)
    
        variants = []
        for entry in data:
                variant = entry[1]
                variant = variant.split(',')
                variants.append(variant)

        right_answers = []
        for entry in data:
                right = entry[2]
                right_answers.append(right)

        variant_kb = InlineKeyboardMarkup(resize_keyboard=True)
        for variant in variants[order_testing]:
                if variant == right_answers[order_testing]:
                        variant_btn = InlineKeyboardButton(variant, callback_data='right')
                else: 
                        variant_btn = InlineKeyboardButton(variant, callback_data='wrong')
                variant_kb.add(variant_btn)
        
        variant_kb.add(InlineKeyboardButton('Следующий вопрос', callback_data='next_testing_question'))
        await bot.send_message(message.from_user.id, questions[order_testing],reply_markup=variant_kb)

async def right_answer(callback_query: types.CallbackQuery):
        global rights
        rights += 1

async def send_next_testing_question(callback_query: types.CallbackQuery):
        global order_testing
        order_testing+=1
        if order_testing<len(questions)-1:
                variant_kb = InlineKeyboardMarkup(resize_keyboard=True)
                for variant in variants[order_testing]:
                        if variant == right_answers[order_testing]:
                                variant_btn = InlineKeyboardButton(variant, callback_data='right')
                        else:
                                variant_btn = InlineKeyboardButton(variant, callback_data='wrong')
                        variant_kb.add(variant_btn)
                if order_testing<len(questions)-2:
                        variant_kb.add(InlineKeyboardButton('Следующий вопрос', callback_data='next_testing_question'))
                else: 
                        variant_kb.add(InlineKeyboardButton('Закончить тестирование', callback_data='next_testing_question'))
                await bot.send_message(callback_query.from_user.id, questions[order_testing],reply_markup=variant_kb)
        else: 
                await bot.send_message(callback_query.from_user.id, 'Результат теста: {0}/{1}'.format(rights, len(questions)-1),\
                         reply_markup=basic_menu)

async def translate_send_first(data, message):
        global translates_rus, translates_btn, translates_right, order_translate, click_words

        order_translate = 0
        click_words = []

        translates_rus = []
        for entry in data:
                rus_sentence = entry[0]
                translates_rus.append(rus_sentence)

        translates_btn = []
        for entry in data:
                wrong_sentence = entry[1]
                wrong_sentence = wrong_sentence.split(',')
                translates_btn.append(wrong_sentence)

        translates_right = []
        for entry in data:
                right_sentence = entry[2]
                right_sentence = right_sentence.split(",")
                translates_right.append(right_sentence)

        sentence = translates_btn[order_translate]

        translates_sentence = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
        
        rus_translate = f'<i>{translates_rus[order_translate]}</i>'

        translate_btn_array = []
        for word in sentence:
                word_btn = InlineKeyboardButton(word, callback_data=str(word))
                translate_btn_array.append(word_btn)
        translates_sentence.row(*translate_btn_array).\
                add(InlineKeyboardButton("Отправить", callback_data='next_translate'))
        msg =  'Переведи предложение и выбери правильную очередность:\n\n' + rus_translate
        await bot.send_message(message.from_user.id, msg, reply_markup=translates_sentence, parse_mode='HTML')    

async def translate_word(callback_query: types.CallbackQuery):
        global click_words
        click_words.append(callback_query.data)

async def translates_sentences(callback_query: types.CallbackQuery):
        global click_words, translates_right, order_translate, laudatory_msg
        laudatory_msg = ['Все верно, молодец!', 'Отлично!', 'Так держать!']

        if click_words in translates_right:
                choice = random.choice(laudatory_msg)
                await bot.send_message(callback_query.from_user.id, choice)
        else:
                msg = 'Неверно, правильный вариант:\n'
                for word in translates_right[order_translate]:
                        msg += f'<i>{word}</i>' + ' '
                await bot.send_message(callback_query.from_user.id,  msg, parse_mode='HTML')
        click_words = []
        
        if order_translate<len(translates_btn)-1:
                order_translate +=1
                sentence = translates_btn[order_translate]
                translates_sentence = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
                translate_btn_array = []
                rus_translate = f'<i>{translates_rus[order_translate]}</i>'
                for word in sentence:
                        word_btn = InlineKeyboardButton(word, callback_data=str(word))
                        translate_btn_array.append(word_btn)
                translates_sentence.row(*translate_btn_array)\
                        .add(InlineKeyboardButton("Отправить", callback_data='next_translate'))
                msg =  'Переведи предложение и выбери правильную очередность:\n\n' + rus_translate
                await bot.send_message(callback_query.from_user.id, msg, reply_markup=translates_sentence, parse_mode="HTML")
        else:
                await bot.send_message(callback_query.from_user.id, 'Вопросы закончились 😅')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(text_message, content_types=['text'])
    dp.register_callback_query_handler(right_answer, text = 'right')
    dp.register_callback_query_handler(translates_sentences, text = 'next_translate')
    dp.register_callback_query_handler(send_next_testing_question, text = 'next_testing_question')
    dp.register_callback_query_handler(translate_word, lambda x: x.data in translates_btn[order_translate])