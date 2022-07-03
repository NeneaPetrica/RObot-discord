import os
import discord
from discord.ext import commands
import random


if len(os.getenv("DISCORD_TOKEN")) < 2:
    TOKEN = str(input("Discord Token: "))
    lang = str(input("Set a language: "))

else:
    TOKEN = os.getenv("DISCORD_TOKEN")
    lang = "en"

bot = commands.Bot(command_prefix="!")
client = discord.Client()

@client.event
async def on_ready():
    print("Bot has connected to Discord")
    activity = discord.Game(name="", type=3)
    await client.change_presence(status=discord.Status.dnd, activity=activity)


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.event
async def on_message(message):

    if lang == 'ro':
            
        if message.content == '!zar':
            await message.channel.send(random.randint(1,6))
        
        if message.content == '!ajutor':
            await message.channel.send(
        "```Sunt noul tau ajutor!\n"
        "Pot face:\n"
        "!zar - pentru a da cu zarul\n"
        "!fraza - O sa deschid carticica cu replici amuzante si o sa spun una\n"
        "Momentan doar atat, dar o sa mai invat chestii noi pe parcurs!\n```")
    
        quotes_file = open('quotes.txt','r')
        quotes = quotes_file.readlines()
    
        temp_quotes = []

        if message.content == '!fraza':
            response = random.choice(quotes)
            await message.channel.send(response)
    else:
        if message.content == '!dice':
            await message.channel.send(random.randint(1,6))
        
        if message.content == '!help':
            await message.channel.send(
        "```Hi! I am here to make your day a bit better!\n"
        "This is what I can do:\n"
        "!dice - Roll a dice\n"
        "!quote - Say one of the quotes from my little book\n"
        "\n```")
    
        quotes_file = open('quotes.txt','r')
        quotes = quotes_file.readlines()
        
    
        temp_quotes = []

        if message.content == '!quote':
            response = random.choice(quotes)
            await message.channel.send(response)

client.run(TOKEN)

