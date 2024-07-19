#bot.send_message(message.chat.id, 'sorry neponel')
from random import  randint
import  telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
TOKEN = '7308853559:AAHaUL_gVFtVB4V4jU4dFEijlBql222ypTk'
bot=telebot.TeleBot(TOKEN)


##############################################################################3
######################################################################################
wran = randint(10, 12)
dran = randint(9, 11)
yran = randint(11,14)

session = {}



class D1:
    def __init__(self, name, armor, dmg, hp):
        self.name = name
        self.armor = armor
        self.dmg = dmg
        self.hp = hp
    def attack(self, enemy, chat_ID):
        bot.send_message(chat_ID,f'{self.name} атакует {enemy.name}')
        dmg = max(self.dmg - enemy.armor, 0)
        bot.send_message(chat_ID, f'Нанесено {dmg} урона')
        enemy.hp = enemy.hp - dmg
        bot.send_message(chat_ID, f'У {enemy.name} осталось {enemy.hp} здоровья')


class Player(D1):
    def info(self, chat_ID):
        bot.send_message(chat_ID, f'Приветсвую {self.name}\n')



@bot.message_handler(commands=['play'])
def send_welcome(message):
    chat_id = message.from_user.id
    session[chat_id] = {}
    session[chat_id]['Enemy'] = None
    player = Player(name=message.from_user.first_name, armor=6, dmg=yran, hp=50)
    Wywern = D1(name='Виверна', armor=3, dmg=wran, hp=50)
    Dagon = D1(name='Дракон', armor=5, dmg=dran, hp=50)
    session[chat_id]['player'] = player
    session[chat_id]['Wywern'] = Wywern
    session[chat_id]['Dagon'] = Dagon
    session[chat_id]['player'].info(chat_id)
    bot.send_message(chat_id, f'Вы последний оставшийся гладиатор на поле боя, это ваша последняя битва, Император даёт вам выбор в последнем противнике.')
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='Виверна', callback_data='button1')
    button2 = InlineKeyboardButton(text='Дракон', callback_data='button2')
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, 'Выберите противника', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda callback: True)
def callback_inline(callback):
    chat_id = callback.from_user.id
    if callback.data == 'button1' and session[chat_id]['Enemy'] == None:
        session[chat_id]['Enemy'] = session[chat_id]['Wywern']
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Атаковать', callback_data='attack')
        keyboard.add(button1)
        bot.send_message(chat_id,  'Выберите действие', reply_markup=keyboard)
    elif callback.data == 'button2' and session[chat_id]['Enemy'] == None:
        session[chat_id]['Enemy'] = session[chat_id]['Dagon']
        keyboard = InlineKeyboardMarkup()
        button2 = InlineKeyboardButton(text='Атаковать', callback_data='attack')
        keyboard.add(button2)
        bot.send_message(chat_id,  'Выберите действие', reply_markup=keyboard)
    elif callback.data == 'attack' and session[chat_id]['Enemy'] != None:
        session[chat_id]['player'].attack(session[chat_id]['Enemy'], chat_id)
        if session[chat_id]['Enemy'].hp > 0:
            session[chat_id]['Enemy'].attack(session[chat_id]['player'], chat_id)
            if session[chat_id]['player'].hp <= 0:
                bot.send_message(chat_id, 'Вы проиграли, чтобы начать заново введите команду /play')
            else:
                keyboard = InlineKeyboardMarkup()
                button1 = InlineKeyboardButton(text='Атаковать', callback_data='attack')
                keyboard.add(button1)
                bot.send_message(chat_id, 'Выберите действие', reply_markup=keyboard)
        else:
            keyboard = InlineKeyboardMarkup()
            bot.send_message(chat_id, 'Вы выйграли, толпа людей арплодирует вам, Император зовёт вас с собой.')
            button1 = InlineKeyboardButton(text='Идти за ним', callback_data='go1')
            keyboard.add(button1)
            bot.send_message(chat_id, 'Выберите действие', reply_markup=keyboard)
    elif callback.data == 'go1':
        keyboard = InlineKeyboardMarkup()
        b1 = InlineKeyboardButton(text = 'Принять',callback_data='b1')
        b2 = InlineKeyboardButton(text = 'Отказаться',callback_data='b2')
        keyboard.add(b1)
        keyboard.add(b2)
        bot.send_message(chat_id, 'Император предлагает вам встпить в элитный легион', reply_markup=keyboard)
    elif callback.data == 'b1':
        bot.send_message(chat_id, 'Вы стали полноправным гражданином, самым знаменитым воином планеты')
    elif callback.data == 'b2':
        bot.send_message(chat_id, 'Император в гневе, вас бросили в темницу, о вас больше никто не вспомнит')










bot.infinity_polling()


















