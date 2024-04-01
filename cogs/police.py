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

    @app_commands.command(name = "delete", description="Deletes messages")
    @app_commands.checks.has_permissions(manage_guild = True)
    async def delete(self, message: discord.Message, messages: int):
        for i in messages:
            await message.delete()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(police(bot))