#Library
import os 
import json

#Load json file
with open('words.json', 'r', encoding='utf-8') as file:
    data=json.load(file)


#Find and show a word 
def find_word(data, word):
    low_Word = word.lower()

    #Validate and show if the word is found 
    if data.get(low_Word):
        print("Palabra encontrada")
        speech = data[low_Word]["part_of_speech"]
        meaning = data[low_Word]["meaning"]
        example = data[low_Word]["example"]
        upperWord = low_Word.upper()
            
        #print(f"Data completa:  {data[low_Word]}")
        print(f"{upperWord} \n Part of the speech: {speech}\n Meaning: {meaning} \n Example: {example}" )

    else:
        print("Sorry, We couldn't find the word")
  
    
    
    
find_word(data, "finish")


    



