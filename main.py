
import discord
import random
client = discord.Client()
from keepalive import keep_alive
import requests
import json


words = [
    "lol", "lmao", "lmfao", "LMAO", "LMFAO", "LOL", "Lol", "Lmfao", "Lmao"
]
words_start = [
    "haha that was funny", "nice one", "hehe",
    "dude there are others words too!!"
]

wording = {"fine", "good", "Fine", "Good", "FINE", "GOOD", "Gud", "gud", "GUD"}
wording2 = ["thats great to hear", "nice"]


sad = ["notgood" , "bakwaas" , "tired" , "notgood" , "bad" , "Bad" ,"BAD" , "fucked up" , "FUCKED UP" , "Fucked up" , "BAKWAAS" , "Bakwaas"]
sadsay = [ 
    "what can i do?" ,
    "toh main kya karu?"
 ]
sal = [
    "thank you", "Thank you", "Thank You", "THANK YOU", "tank u", "tank you",
    "Tank you", "TANK U "
]
sal_say = "No Problemo"

d = ['wassup', 'WASSUP', 'Wassup']
BOss = ['Rishit' , 'RISHIT' , 'rishit']

alapha = 'a b c d e f g h i j k l m n o p q r s t u v w x y x'

number = '1 2 3 4 5 6 7 8 9 ...n'


def get_quote():
    tpp = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(tpp.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def get_joke():
    response = requests.get(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single"
    )
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return (joke)

def get_snews():
    sak = requests.get(
        "https://www.republicworld.com/sports-news"
    )
    json_data = json.loads(sak.text)
    snews = json_data["snews"]
    return (snews)



@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        await message.channel.send('Hi! how are you?')
    if any(word in message.content for word in words):
        await message.channel.send(random.choice(words_start))
    if any(word in message.content for word in wording):
        await message.channel.send(random.choice(wording2))
    if any(word in message.content for word in sad):
        await message.channel.send(random.choice(sadsay))
    if message.content.startswith('?help'):
        await message.channel.send(
            'Hi! u can send messages starting with ? for example ?hello , ?ping , ?fun.,?inpire,?joke,?'
        )
    if message.content.startswith('?Hello'):
        await message.channel.send('Hi! how are you?')
    if message.content.startswith('?HELLO'):
        await message.channel.send('Hi! how are you?')
    if message.content.startswith('?ping'):
        await message.channel.send('Pinging \n {}'.format(
            message.author.mention))
    if message.content.startswith('?play'):
        await message.channel.send(
            'srry we are work in progress!GAMES WILL BE HERE SOON')

    if message.content.startswith('nothing'):
        await message.channel.send('OK!')
    if message.content.startswith('?hi'):
        await message.channel.send('Hi! how are you?')
    if any(word in message.content for word in sal):
        await message.channel.send(sal_say)
    if message.content.startswith('?wassup'):
        await message.channel.send('Hi! how are you?')
    if any(word in message.content for word in d):
        await message.channel.send('Ayo ! Wassup how is ur day?')
    if message.content.startswith('?alpha'):
        await message.channel.send(alapha)
    if message.content.startswith('?num'):
        await message.channel.send(number)
    if message.content.startswith('??'):
        await message.channel.send("wrong syntax")
    if message.content.startswith('dude'):
        await message.channel.send("yes im a dude ik")
    if message.content.startswith('?inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('?joke'):
        joke = get_joke()
        await message.channel.send(joke)
    if message.content.startswith('?snews'):
        snews = get_snews()
        await message.channel.send(snews)

    if message.content.startswith('?OP'):
        await message.channel.send("https://youtu.be/dQw4w9WgXcQ")
  
    if message.content.startswith('joke'):
        await message.channel.send("A joke umM  " + "jiggy's mum ") 

    if ("paper") in message.content:
        emoji = "😭"
        await message.add_reaction(emoji)
    if ("join") in message.content:
        demoji = "👍"
        await message.add_reaction(demoji)
    if ("love") in message.content:
        emoji = "💋"
        await message.add_reaction(emoji)
    if ("lol") in message.content:
        emoji = "😀"
        await message.add_reaction(emoji)
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "👾"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "👽"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😬"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🙄"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😯"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😧"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😮"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😲"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😴"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤤"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😪"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤢"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤧"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😷"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💩"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤡"
        await message.add_reaction(emoji)
    if ("paper") in message.content:
        emoji = "😭"
        await message.add_reaction(emoji)
    if ("join") in message.content:
        emoji = "👍 "
        await message.add_reaction(emoji)
    if ("love") in message.content:
        emoji = "💋"
        await message.add_reaction(emoji)
        emoji = "😀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "👾"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "👽"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😬"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🙄"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😯"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😧"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😮"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😲"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😴"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤤"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😪"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤢"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤧"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😷"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💩"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤡"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "👾"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "👽"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😬"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🙄"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😯"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😧"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😮"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😲"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😴"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤤"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😪"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤢"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤧"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "😷"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💩"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("bruh") in message.content:
        emoji = "🤡"
        await message.add_reaction(emoji)

    if ("Bruh") in message.content:
        emoji = "👾"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "👽"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😬"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "🙄"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😯"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😧"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😮"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😲"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😴"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "🤤"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😪"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "🤢"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "🤧"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "😷"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "💩"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("Bruh") in message.content:
        emoji = "🤡"
        await message.add_reaction(emoji)

    if ("BRUH") in message.content:
        emoji = "👾"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "👽"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😬"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "🙄"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😯"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😧"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😮"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😲"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😴"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "🤤"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😪"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "🤢"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "🤧"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "😷"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "💩"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "💀"
        await message.add_reaction(emoji)
    if ("BRUH") in message.content:
        emoji = "🤡"
        await message.add_reaction(emoji)
    
    if ("stfu") in message.content:
        kol = "🖕"
        await message.add_reaction(kol)

    if message.content.startswith('noice'):
      await message.channel.send('ik')


    if any(word in message.content for word in BOss):
        await message.channel.send("HE IS MY BOSS")

    if message.content.startswith("Harman"):
        await message.channel.send('<@325747010324135946>')

    if message.content.startswith("Ashmit"):
        await message.channel.send('<@778853917927931914>') 

    if message.content.startswith("Ojas"):
        await message.channel.send('<@365481836924633088>') 

    if message.content.startswith("Nishant"):
        await message.channel.send('<@803278409219702835>') 

    if message.content.startswith("Jignesh"):
        await message.channel.send('<@705451492391387197>') 












keep_alive()
client.run('{*****************************************************}')
