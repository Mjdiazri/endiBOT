#Libraries
import os 
import json

#Global variable
word = "word"

#Load json file
with open('words.json', 'r', encoding='utf-8') as file:
    data=json.load(file)


#Interaction chatbot
def start():
    name = input("Hi! Please insert your name:  ")
    global word 
    word = input(f"Welcome {name}!, I can help you to look up words meaning, what word do you like I search?  ")
    find_word()

def ask():
    decision = input("Would you like look up for another word?")
    global decision_low
    decision_low= decision.lower()
    

def loop():
    affirmative = ['yes', 'y', 'yep', 'certainly', 'yeah', 'yup', 'sure', 'Okay', 'ok', 'alright', 'totally']

    ask()
    while decision_low in affirmative:
        global word
        word = input('Lets do it, what word do you want look up?')
        find_word()
        ask()
    
    print('Ok! see you later aligater') 
    
    
#Find and show a word 
def find_word():
    low_Word = word.lower()

    #Validate and show if the word is found 
    if data.get(low_Word):
        
        speech = data[low_Word]["part_of_speech"]
        meaning = data[low_Word]["meaning"]
        example = data[low_Word]["example"]
        upperWord = low_Word.upper()
            
        #print(f"Data completa:  {data[low_Word]}")
        print(f"{upperWord} \n Part of the speech: {speech}\n Meaning: {meaning} \n Example: {example}" )

    else:
        print("Sorry, We couldn't find the word")
  
    

start() 
loop()

 



    



