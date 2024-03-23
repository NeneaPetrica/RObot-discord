import discord
from discord import app_commands
from discord.ext import commands
from discord import *

class filtermod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if 'https://www.instagram.com/' in message.content.lower():
            message.delete()
            await message.channel.send('FilterMod: Instagram posts are not allowed on the server.')


async def setup(bot):
    await bot.add_cog(filtermod(bot))