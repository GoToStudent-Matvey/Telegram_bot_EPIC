import telebot
from random import choice
token="664340610:AAG0eeJ-mKtKusIillg19e96Tta4xlL6ip8"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
anekdots = []
anekdot1 = "Какая разница между коммунистом и антикоммунистом?\n Коммунист - это человек прочитавший работы Маркса и Ленина.\n А антикоммунист - это тот, кто их понял."
anekdot2 = "Брежнев и Черненко беседуют на том свете:\n Костя, а кто сейчас вместо нас правит?\n Да Миша Горбачев.\n А кто его поддерживает?\n А чего его поддерживать? Он пока сам ходит."
anekdot3 = "Ленин и Брежнев встречаются на том свете. Брежнев спрашивает:\n Ты там чего-нибудь строил?\n Нет, а ты?\n Тоже нет. Что он там перестраивает?"
anekdots.append(anekdot1)
anekdots.append(anekdot2)
anekdots.append(anekdot3)
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=["start","help"])
def help(message):
    user = message.chat.id
    bot.send_message(user,"Напиши /anek и я пришлю случайный анекдот")

@bot.message_handler(commands=["anek"])
def anekdot(message):
    user = message.chat.id
    text=choice(anekdots)
    bot.send_message(user,text)

@bot.message_handler(content_types=['text'])
def ranmes(message):
    user=message.chat.id
    text=('Я те попугай что-ли? Сам с собой поговоришь!')
    bot.send_message(user, text)

bot.polling(none_stop=True)
