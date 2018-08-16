import telebot
from random import randint
token="664340610:AAG0eeJ-mKtKusIillg19e96Tta4xlL6ip8"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)

z=0
@bot.message_handler(commands=["help"])
def help(message):
    user = message.chat.id
    bot.send_message(user,"Это бот Угадайка.Напиши /start и отгадай число")
@bot.message_handler(commands=["start"])
def start(message):
    global z
    user = message.chat.id
    z=randint(0,71)
    bot.send_message(user,"Угадай число!")
    

@bot.message_handler(content_types=['text'])
def guess(message):
    global z
    user = message.chat.id
    try:
        var=int(message.text)
        if var==z:
            text='Угадал!Я загадал следующее число.'
            z=randint(0,71)
        elif var<z:
            text='Больше'
        else:
            text='Меньше'
    except ValueError:
        text='ТЫ ОФИГЕЛ!!ПИШИ ЦИФРУ,А ТО ПОЗОВУ МОМО!!!'
    bot.send_message(user,text)

bot.polling(none_stop=True)
