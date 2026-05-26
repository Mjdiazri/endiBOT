import os
import telebot
import json
from dotenv import load_dotenv


#Read .env Telegram token
load_dotenv()
TOKEN= os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

#Load json file
with open('words.json', 'r', encoding='utf-8') as file:
    data=json.load(file)

#Start chatbot
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hi, welcome to EndiBOT. I can help you to look up word meanings, what word do you like I search?')
   


#Check request
#bot.infinity_polling() 
print('EndiBOT started.....')

