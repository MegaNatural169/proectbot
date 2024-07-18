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


class D1:
    def __init__(self, name, armor, dmg, hp):
        self.name = name
        self.armor = armor
        self.dmg = dmg
        self.hp = hp
    def attack1(self):
        print(f'вас атакует{Wywern.name}')
        You.hp = You.hp - (Wywern.dmg - You.armor)

Wywern = D1(name = 'Виверна', armor = 3, dmg = wran , hp =50)

class D2:
    def __init__(self, name, armor, dmg, hp):
        self.name = name
        self.armor = armor
        self.dmg = dmg
        self.hp = hp
    def attack2(self):
        print(f'вас атакует{Dagon.name}')
        You.hp = You.hp - (Dagon.dmg - You.armor)


Dagon = D2(name = 'Дракон', armor = 5, dmg = dran, hp =50)

class You:
    def __init__(self, armor, dmg, hp):
        self.armor = armor
        self.dmg = dmg
        self.hp = hp
    def attacking2(self):
        print(f'вы атаковали{Dagon.name}')
        Dagon.hp = Dagon.hp - (You.dmg - Dagon.armor)
    def attacking1(self):
        print(f'вы атаковали{Wywern.name}')
        Wywern.hp = Wywern.hp - (You.dmg - Wywern.armor)
    def die1(self):
        print(f'вы победили{Wywern.name}')
    def die2(self):
        print(f'вы победили{Dagon.name}')
    def die3(self):
        print(f'вас победил{Dagon.name}')
    def die4(self):
        pint(f'вас победил{Wywern.name}')

Player = You(armor =6, dmg = yran, hp =50 )

@bot.message_handler(commands=['play'])
def send_welcome(message):
    bot.send_message = (chat.message.id, 'хотите играть')
    if 'да' or 'ок' in message.text.lower():
        bot.register_next_step_handler(message.chat.id, next1)
    else:
        bot.send_message(message.chat.id, 'я вас понял')

def next1:
    bot.send_message(message.chat.id, 'выберите противника')
    markup = types.Inline





















