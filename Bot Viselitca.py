import telebot
from random import choice

token="664340610:AAG0eeJ-mKtKusIillg19e96Tta4xlL6ip8"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)

available_words = ['Яблоко', 'Груша', 'Дыня','Арбуз', 'Персик', 'Ананас', 'Клубника', 'Малина', 'Слива', 'Абрикос', 'Xумус']
user_word = {}
user_letters_left = {}
user_lifes = {}

@bot.message_handler(commands=["help"])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Это бот Виселица.Напиши /start и отгадай слово, написав одну букву.\nУ вас есть 7 попыток." )

@bot.message_handler(commands=["start"])
def start(message):
    global available_words
    global user_word
    global user_lifes
    user = message.chat.id
    word = choice(available_words)
    word = word.lower()
    if user in user_word:
        user_word.update([user, word])
        user_position.update([user, 0])
        lifes.update([user, 7])
    else:
        user_lifes[user] = 7
        user_word[user] = word
    bot.send_message(user,"Угадай слово!")
    

@bot.message_handler(content_types=['text'])
def guess(message):
    global available_words
    global user_word
    global user_letters_left
    global user_lifes
    user=message.chat.id
    bot.send_message(user,user_word[user])    
    if user_lifes[user] != 0:
        bot.send_message(user, 'You have: ' + str(user_lifes[user]))
    else:
        bot.send_message(user, 'You have: ' + "You have no lifes please /start to play again")
        return

    if len(message.text) != 1:
        bot.send_message(user, 'Please enter only ONE letter')
        return
    let = message.text
    
    if let.lower() not in user_word[user]:
        user_lifes.update([user_lifes[user],user_lifes[user] - 1])
        return
     
    if let.lower() in user_word[user]:
        shrink = user_word[user].split(let.lower())
        wordWithout=user_word[user]
        for part in shrink:
            wordWithout+=part
        user_word.update(user_word[user], wordWithout)
            
bot.polling(none_stop=True)
