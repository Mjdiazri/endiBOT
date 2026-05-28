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
    print('loading json file.....')

#Start chatbot
@bot.message_handler(commands=['start'])
def start(message):
    name = message.chat.first_name  
    bot.send_message(message.chat.id, f"Hey {name}, welcome to EndiBOT!!! I can look up word meanings.")
    msg=bot.send_message(message.chat.id, "Type a word for help you.... ")   
    bot.register_next_step_handler(msg,send_response ) 

#Chatbot Interaction
@bot.message_handler(content_types=['text'])
def send_response(message):
        print('comming message....')
        global word
        word = message.text
        find_word()
        bot.send_message(message.chat.id, f"{upperWord} \n Part of speech: {speech}\n Meaning: {meaning}\n Example: {example}")
        bot.send_message(message.chat.id, "Would you like to look up another word?     /sure  ||  /nop ")  

@bot.message_handler(commands=['sure'])
def loop(message):
     bot.send_message(message.chat.id, "Please type the word for looking...")
     send_response()     


# look up the word    
def find_word():
    low_Word = word.lower()
    print(f"Searching for {low_Word}.....")

    #Validate if the word is found 
    if data.get(low_Word):
        #Validation
        print("I got the word....")
        
        global speech 
        global meaning
        global example
        global upperWord
        
        speech = data[low_Word]["part_of_speech"]
        meaning = data[low_Word]["meaning"]
        example = data[low_Word]["example"]
        upperWord = word.upper()
    else:
        print("You got me! I dont found the word")
        #develop code for show that the word dont was found and retur to loop function






   

#Check request and status
print('EndiBOT started.....')   
bot.infinity_polling()