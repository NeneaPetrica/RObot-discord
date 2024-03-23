import os
import discord
from discord.ext import commands
import random
import asyncio

token_file = open("token.txt", "r")
TOKEN = str(token_file.read())
token_file.close()

intents=discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="/", intents = intents, help_command= None)

#def writeHugs(user_id, hugs = int):
#    file = open(f"./bank/{user_id}.txt", "r")
#    temp_int = int(file.read())
#    file = open(f"./bank/{user_id}.txt", "w")
#    file.write(str(temp_int + hugs))
#    file.close()


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print("Bot has connected to Discord")
    activity = discord.Game(name="/help", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())