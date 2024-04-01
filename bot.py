import os
import discord
from discord.ext import commands
import random
import asyncio
import subprocess

token_file = open("token.txt", "r")
TOKEN = str(token_file.read())
token_file.close()

intents=discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all(), help_command= None)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def reload():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.reload_extension(f"cogs.{filename[:-3]}")

async def unload():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.unload_extension(f"cogs.{filename[:-3]}")
        
@bot.event
async def on_ready():
    print("Bot has connected to Discord")
    activity = discord.Game(name="/help", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)!")
    except Exception as e:
        print(e)

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())


