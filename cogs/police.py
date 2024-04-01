from discord.ext import commands
import discord
from discord import app_commands
import os
import random

class core(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading core...")

    @app_commands.command(name = "hello", description= "Toggles the social media filter")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi, {interaction.user.mention}!")

    @app_commands.command(name = "dice", description= "Rolls a dice")
    async def dice(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.randint(1, 6))

    @app_commands.command(name = "delete", description= "Deletes messages")
    async def delete(self, selection: 0, interaction: discord.Interaction, message: discord.Message):
        for i in selection:
            await message.delete()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(core(bot))