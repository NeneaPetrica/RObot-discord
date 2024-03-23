from discord.ext import commands
import discord
from discord import app_commands
import os

class filtermod(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Filter is ready")
        
    async def on_message(self, message: discord.Message, interaction: discord.Interaction):
        if 'https://www.instagram.com/' in message.content.lower():
            file = open(f"./configs/{interaction.guild.id}.txt", "r")
            temp_int = int(file.read())
            if temp_int == 1:
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            else:
                print(f"Guild {interaction.guild.id} has filter turned off")

    @app_commands.command(name = "togglefilter", description= "What? It works????")
    async def togglefilter(self, interaction: discord.Interaction):
        if os.path.isfile(f"./configs/{interaction.guild.id}-filter.txt") == False:
            file = open(f"./configs/{interaction.guild.id}-filter.txt", "w")
            file.write(str(1))
            file.close()
            print("Created FilterMod File")

        file = open(f"./configs/{interaction.guild.id}-filter.txt", "r")
        temp_int = int(file.read())

        if temp_int == 0:
            file = open(f"./configs/{interaction.guild.id}-filter.txt", "w")
            file.write(str(1))
            file.close()
            await interaction.response.send_message("Filter is now turned on for this server.")
        else:
            file = open(f"./configs/{interaction.guild.id}-filter.txt", "w")
            file.write(str(0))
            file.close()
            await interaction.response.send_message("Filter is now turned off for this server.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(filtermod(bot))