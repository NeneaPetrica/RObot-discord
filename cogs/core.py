from discord.ext import commands
import discord
from discord import app_commands
import os

class core(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
        print("Loading core...")

    @app_commands.command(name = "hello", description= "Toggles the social media filter")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi, {interaction.user.mention}!")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(core(bot))