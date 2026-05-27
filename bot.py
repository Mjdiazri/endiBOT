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
    name = message.chat.first_name   

    bot.send_message(message.chat.id, f"Hi {name}, welcome to EndiBOT!!! I can look up word meanings.")
    word= bot.send_message(message.chat.id, "Type a word for help you.... ")
   

#Check request and status
print('EndiBOT started.....')   
bot.infinity_polling() 


