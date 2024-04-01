from discord.ext import commands
import discord
from discord import app_commands
import os
import random

class police(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading police.py...")

    @app_commands.command(name = "delete", description= "Deletes messages")
    async def delete(self, selection: 0, interaction: discord.Interaction, message: discord.Message):
        for i in selection:
            await message.delete()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(police(bot))