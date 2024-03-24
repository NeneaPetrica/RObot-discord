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
        await print("Loading quotes...")

    @app_commands.command(name = "register_quotebook", description= "Makes a server quotebook")
    async def register_quotebook(self, interaction: discord.Interaction):
        quotes_file = open(f'./quotes/{interaction.guild.id}-quotes.txt', 'w')
        await interaction.response.send_message("A quotebook for the server has been created.")

    @app_commands.command(name = "quote", description= "Says a quote")
    async def quote(self, interaction: discord.Interaction):
        try:
            quotes_file = open(f"./quotes/{interaction.guild.id}-quotes.txt", 'r')
            quotes = quotes_file.readlines()
            temp_quotes = []
            response = random.choice(quotes)
            await interaction.response.send_message(response)
        except:
            await interaction.response.send_message("Your server does not have a quote book. To create one use the command: /register_quotebook")

    @app_commands.command(name = "add_quote", description= "Adds a quote to the quotebook")
    async def add_quote(self, interaction: discord.Interaction, new_quote: str):
        quotes_file = open(f"./quotes/{interaction.guild.id}-quotes.txt", 'a')
        quotes_file.write(new_quote)
        await interaction.response.send_message(f"You added the quote: {new_quote}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(core(bot))