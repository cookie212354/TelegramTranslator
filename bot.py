import telebot
from googletrans import Translator
#pip install telebot, googletrans==4.0.0rc1
BOT_TOKEN = 'tokenforbot'
bot = telebot.TeleBot(BOT_TOKEN)

translator = Translator()
@bot.message_handler(commands=['start'])
def startup(message):
    bot.send_message(message.chat.id,"Использование: /translate > Иностранное слово <")

@bot.message_handler(commands=['translate'])
def translate_message(message):
    try:
        text = message.text.split(' ', 1)[1]
    except:
        bot.send_message(message.chat.id,"Ошибка, Введите хотя-бы одно предложение или слово.")
        return
    
    src = translator.detect(text).lang
    
    translation = translator.translate(text, src=src, dest='ru')
        
    bot.reply_to(message, f"Перевод: {translation.text}")

print("Bot started. Waiting for messages...")
bot.polling()
