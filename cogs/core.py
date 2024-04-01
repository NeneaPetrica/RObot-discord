from discord.ext import commands
import discord
from discord import app_commands
import os
import random
from economy import economyHelp

coreHelp = """\n ==== Small Commands ====\n
                /hello - Says hi to you :)\n
                /dice - Roll a dice\n"""

class core(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        print("Loading core...")

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading core...")

    @app_commands.command(name = "hello", description= "Toggles the social media filter")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi, {interaction.user.mention}!")

    @app_commands.command(name = "dice", description= "Rolls a dice")
    async def dice(self, interaction: discord.Interaction):
        await interaction.response.send_message(random.randint(1, 6))

    @app_commands.command(name = "poke", description= "Pokes the specified user")
    async def poke(self, interaction: discord.Interaction, user: discord.Member = None):
        pokeArray = ["https://media1.tenor.com/m/_C06NtBa8pcAAAAC/mochi-poke-poke-cute-cat.gif",
                     "https://media1.tenor.com/m/hlrUN-PqmpsAAAAd/seals-yo-chan.gif",
                     "https://media1.tenor.com/m/o9X9XXVCm-MAAAAd/bird-cute.gif"]
        
        gif = pokeArray[random.randint(0,3)]

        await interaction.response.send_message(f"{interaction.user.mention} poked <@{user.id}>!"
                                                "\n"
                                                f"{gif}")

    @app_commands.command(name = "help", description= "Tells what AstroBot can do")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(
                "```Hi, my name is AstroBot! I am here to make your day a bit better!\n"
                "This is what I can do:\n \n"

                f"{coreHelp}"
                f"{quoteHelp}"
                f"{economyHelp}"
                "\n```")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(core(bot))