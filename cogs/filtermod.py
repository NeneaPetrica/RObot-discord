import os
import discord
from discord import app_commands
from discord.ext import commands
from discord import *
import random
import ctypes
import asyncio

class FliterMod_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        if 'https://www.instagram.com/' in message.content.lower():
            await message.delete()
            await message.channel.send('FilterMod: Instagram posts are not allowed on the server.')
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello')


async def setup(bot):
    await bot.add_cog(FliterMod_cog(bot))