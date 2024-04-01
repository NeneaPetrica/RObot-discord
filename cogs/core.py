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

    @app_commands.command(name = "help", description= "Tells what AstroBot can do")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(
                "```Hi, my name is AstroBot! I am here to make your day a bit better!\n"
                "This is what I can do:\n \n"

                "\n ==== Small Commands ====\n"
                "/hello - Says hi to you :)\n"
                "/dice - Roll a dice\n"
                
                "\n ==== Quote books ====\n"
                "/register-quotebook - Makes a special quotebook for the server \n"
                "/add_quote {new_quote} - Adds a quote to the server quotebook \n"
                "/quote - Says a random quote from the server quotebook \n"
                
                "\n ==== HugBank ====\n"
                "/hug_register - Registers you to HugBank\n"
                "/hug {tag a user} - Sends a hug to the hugged user\n"
                "/balance - See the hug balance\n"

                "\n ==== Gambling ====\n"
                "/slotmachine - You play slots and can win Hugs!\n \n"

                "Slots Prizes: \n"
                ">🍇|🍇|🍇< for 500 hugs\n"
                ">🍒|🍒|🍒< for 1000 hugs\n"
                ">🍓|🍓|🍓< for 1250 hugs\n"
                ">🍉|🍉|🍉< for the JACKPOT (which is secret)\n \n"

                "/all_in - Doubles your Hugs or lose them all.\n"
                "\n```")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(core(bot))