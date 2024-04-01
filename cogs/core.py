from discord.ext import commands
import discord
from discord import app_commands
import os
import random

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
"""```
Hi, my name is AstroBot! I am here to make your day a bit better!\n
This is what I can do:\n

 ==== Moderation ====\n
/togglefilter - Toggles a pre-defined social media filter. If is on, posts from Instagram will be instantly deleted. \n
/delete {messages} - Deletes the specified number of messages \n

==== Small Commands ==== \n
/hello - Says hi to you :) \n
/dice - Roll a dice \n
/poke {user} - Pokes the mentioned user \n
                
==== Quote books ====\n
/register-quotebook - Makes a special quotebook for the server \n
/add_quote {new_quote} - Adds a quote to the server quotebook \n
/quote - Says a random quote from the server quotebook \n
                
==== HugBank ====\n
/hug_register - Registers you to HugBank\n
/hug {user} - Sends a hug to the hugged user\n
/balance - See the hug balance\n

==== Gambling ====\n 
/slots - You play slots and can win Hugs!\n
\n Slots Prizes:\n
>🍇|🍇|🍇< for 500 hugs\n
>🍒|🍒|🍒< for 1000 hugs\n
>🍓|🍓|🍓< for 1250 hugs\n
>🍉|🍉|🍉< for the JACKPOT (which is secret)\n\n
/all_in - Doubles your Hugs or lose them all.\n
\n```""")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(core(bot))