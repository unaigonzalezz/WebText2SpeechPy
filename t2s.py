from newspaper import Article
import nltk
from gtts import gTTS
import os

print("""
____________________  _________   ______________     _______________________________________________  __
___  __/__  ____/_  |/ /__  __/   ___  __/_  __ \    __  ___/__  __ \__  ____/__  ____/_  ____/__  / / /
__  /  __  __/  __    /__  /      __  /  _  / / /    _____ \__  /_/ /_  __/  __  __/  _  /    __  /_/ / 
_  /   _  /___  _    | _  /       _  /   / /_/ /     ____/ /_  ____/_  /___  _  /___  / /___  _  __  /  
/_/    /_____/  /_/|_| /_/        /_/    \____/      /____/ /_/     /_____/  /_____/  \____/  /_/ /_/                                                                                                   
""")
print(""" by:
  _   _           _    ___               __ _        
 | | | |_ _  __ _(_)  / __|___ _ _  ____/_/| |___ ___
 | |_| | ' \/ _` | | | (_ / _ \ ' \|_ / _` | / -_)_ /
  \___/|_||_\__,_|_|  \___\___/_||_/__\__,_|_\___/__|
""")

article = Article(input("Enter a link of an article to convert text to speech:" ))
print("Loading... Please wait :) ")
article.download()
article.parse()
nltk.download('punkt', quiet=True)
article.nlp()
mytext = article.text

print("""
 1.English
 2.Spanish
 3.Portuguese
 4.Italian
 5.French
 """)
languagechoose = int(input("In what language is the article written?:"))


if languagechoose == 1:
    language = ("en")
    print("You have chosen English!")

if languagechoose == 2:
    language = ("es")
    print("You have chosen Spanish!")

if languagechoose == 3:
    language = ("pt")
    print("You have chosen Portuguese!")

if languagechoose == 4:
    language = ("it")
    print("You have chosen Italian!")

if languagechoose == 5:
    language = ("fr")
    print("You have chosen French!")

print("Loading... Please wait :) ")
print("May be slow if the article is too long")
print("The article will start automatically when converted")
obj = gTTS(text=mytext, lang=language, slow=False)
obj.save("article.mp3")
os.system("start article.mp3")

print("Finished... Thanks for using my code! :D")



