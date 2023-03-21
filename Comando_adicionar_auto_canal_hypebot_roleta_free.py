import telebot
from telebot import types

# Insira o token do seu bot do Telegram
bot_token = "6251992139:AAEmyp6c8VO4xQqDOrwaXuOFk5GBq9DafXE"

# Insira o ID do seu canal do Telegram
channel_id = "-1001621745674"

bot = telebot.TeleBot(bot_token)

# Define a função que adiciona o usuário ao canal
def add_to_channel(chat_id):
    try:
        bot.send_message(chat_id, "Obrigado por se inscrever no meu HYPE Bot!")
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, "Você será adicionado automaticamente ao canal em breve.")
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, "Obrigado por confiar em nosso trabalho e bons lucros!")
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, "Atenciosamente, seu mentor em apostas, o Hypado!")
        bot.invite_chat_member(channel_id, chat_id)
    except Exception as e:
        print(e)

# Define a função que recebe as atualizações de usuários que se inscrevem no bot
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    add_to_channel(chat_id)

bot.polling()
