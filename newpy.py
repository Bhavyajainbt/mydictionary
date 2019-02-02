import json
import difflib
from difflib import get_close_matches

file = open("first.json","r")
file = json.load(file)

def translate(w):
    w = w.lower()
    if w in file:
         return file[w]
    elif len(get_close_matches(w, file.keys())) > 0:
         yn = input("did you mean %s instead? Enter Y if yes,or N if no:" % get_close_matches(w,file.keys())[0])
         if yn == "Y":
             return file[get_close_matches(w,file.keys())[0]]
         elif yn == "N":
             return "The word doesn't exist.please double check it."
         else:
             return "We didn't understand your query."
    else:
         return "The word does not exist in the dictionary.Please check your spelling again."


word = input("Enter your word:")
print(translate(word))
