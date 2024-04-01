import discord
from discord.ext import commands
from discord import app_commands
import random

class economy(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading police.py...")
    
    @app_commands.command(name="slots", description="Get more hugs from gambling!")
    async def slots(self, interaction: discord.Interaction):
        emoteArray = []

        for i in range(3):
            temp_val = random.randint(1,4)

            if(temp_val == 1):
                temp_emote = ":grapes:"
            elif(temp_val == 2):
                temp_emote = ":cherries:"
            elif (temp_val == 3):
                temp_emote = ":strawberry:"
            else:
                temp_emote = ":watermelon:"
            
            emoteArray.append(temp_emote)
            
        emote1 = str(emoteArray[0])
        emote2 = str(emoteArray[1])
        emote3 = str(emoteArray[2])

        if (emote1 == ":grapes:" and emote2 == ":grapes:" and emote3 == ":grapes:"):
            writeHugs(interaction.user.id, 500)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 500 hugs!")

        elif (emote1 == ":cherries:" and emote2 == ":cherries:" and emote3 == ":cherries:"):
            writeHugs(interaction.user.id, 1000)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 1000 hugs!")

        elif (emote1 == ":strawberry:" and emote2 == ":strawberry:" and emote3 == ":strawberry:"):
            writeHugs(interaction.user.id, 1250)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 1250 hugs!")

        elif (emote1 == ":watermelon:" and emote2 == ":watermelon:" and emote3 == ":watermelon:"):
            writeHugs(interaction.user.id, 100000)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 100,000 hugs! JACKPOT!")
        else:
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n Better luck next time!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(economy(bot))