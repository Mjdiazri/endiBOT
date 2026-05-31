import os
import telebot
import json
from dotenv import load_dotenv



#Read
load_dotenv()
TOKEN= os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

#Load json file
with open('words.json', 'r', encoding='utf-8') as file:
    data=json.load(file)
    print('loading json file.....👾🤖🔎🔍📌🔹🔸▫️')

#Start chatbot
@bot.message_handler(commands=['start'])
def start(message):
    name = message.chat.first_name  
    bot.send_message(message.chat.id, f"Hey {name}, welcome to EndiBOT👾!!! I can look up word meanings.")
    msg=bot.send_message(message.chat.id, "📚Type a word and I'll help you find its meaning...")   
    bot.register_next_step_handler(msg,send_response) 

#Chatbot Interaction
@bot.message_handler(content_types=['text'])
def send_response(message):
        print('comming message....')
        word = message.text
        founded = find_word(word)

        if founded["isFound"] == True:
            bot.send_message(message.chat.id, f"{founded['upperWord']} \n 🔸Part of speech: {founded['speech']}\n 🔸Meaning: {founded['meaning']}\n 🔸Example: {founded['example']}")
            msg = bot.send_message(message.chat.id, "Would you like to look up for another word?🔍  /sure   ||      /nop")      
            bot.register_next_step_handler(msg,loop_word)  
        else:
            bot.send_message(message.chat.id, "Sorry, I couldn't find that word.")
            msg = bot.send_message(message.chat.id, "Would you like to look up another word?🔍  /sure   ||      /nop")      
            bot.register_next_step_handler(msg,loop_word)
            

#Loop
def loop_word(message):
     decision = message.text.lower()
     if decision == "/sure":
          print("The word is /sure")
          msg=bot.send_message(message.chat.id, "Please type the word 📖")
          bot.register_next_step_handler(msg,send_response)           
     elif decision == "/nop":
          print("The word is /nop") 
          bot.send_message(message.chat.id, "👾See you later, aligater")
     else:
          print("Unfounded word")
          bot.send_message(message.chat.id, "👾I can't understand you, See you soon")

# look up the word    
def find_word(word):
    low_Word = word.lower()
    print(f"Searching for {low_Word}.....")
    if data.get(low_Word):
        #Validation
        print("I got the word....")
        return{
            "isFound": True,
            "speech": data[low_Word]["part_of_speech"],
            "meaning": data[low_Word]["meaning"],
            "example": data[low_Word]["example"],
            "upperWord": word.upper()             
        }       
    else:
        print("You got me! I dont found the word")
        return{
             "isFound": False
        }
   

#Check request and status
print('EndiBOT started.....')   
bot.infinity_polling()