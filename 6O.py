import telebot

BOT_TOKEN = "6108579220:AAEAxB4Bpe8WxsT6d5KrVWeKUqHN0q8Brag"

bot = telebot.TeleBot(BOT_TOKEN)

commands = {
    "tell": None
}

def command_parser(msg):
    if msg == "test":
        return "I've successfuly read the command."
    elif not msg:
        return "What is your request?"
    elif msg == "hosting":
        return "I am currently hosted by replit.com"
    else:
        return "I don't recognize this command."

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    #bot.reply_to(message, "Howdy, how are you doing?")
    pass

@bot.message_handler(func=lambda msg: True, chat_types="group")
def echo_all(message):
    #bot.reply_to(message, message.text)
    pass

@bot.message_handler(commands=['operator'])
def basic_reply(message):
    command = command_parser(message.text.removeprefix('/operator '))
    bot.reply_to(message, command)

bot.infinity_polling()