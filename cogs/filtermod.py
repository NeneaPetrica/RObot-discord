from discord.ext import commands
import discord
from discord import app_commands
import os

class filtermod(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        print("Loading filters...")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if 'https://www.instagram.com/' in message.content.lower():
            file = open(f"./configs/{message.guild.id}-filter.txt", "r")
            temp_int = int(file.read())

            if temp_int == 1:
                file.close()
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            if temp_int == 0:
                file.close()
                await print(f"Guild {message.guild.id} has filter turned off")

        if 'https://w.instagram.com/' in message.content.lower():
            file = open(f"./configs/{message.guild.id}-filter.txt", "r")
            temp_int = int(file.read())

            if temp_int == 1:
                file.close()
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            if temp_int == 0:
                file.close()
                await print(f"Guild {message.guild.id} has filter turned off")

        if 'https://ww.instagram.com/' in message.content.lower():
            file = open(f"./configs/{message.guild.id}-filter.txt", "r")
            temp_int = int(file.read())

            if temp_int == 1:
                file.close()
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            if temp_int == 0:
                file.close()
                await print(f"Guild {message.guild.id} has filter turned off")

        if 'https://instagram.com/' in message.content.lower():
            file = open(f"./configs/{message.guild.id}-filter.txt", "r")
            temp_int = int(file.read())

            if temp_int == 1:
                file.close()
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            if temp_int == 0:
                file.close()
                await print(f"Guild {message.guild.id} has filter turned off")


    @app_commands.command(name = "togglefilter", description= "Toggles the social media filter")
    @app_commands.checks.has_permissions(manage_guild = True)
    async def togglefilter(self, interaction: discord.Interaction):
        if os.path.isfile(f"./configs/{interaction.guild.id}-filter.txt") == False:

            file = open(f"./configs/{interaction.guild.id}-filter.txt", "w")
            file.write(str(1))
            file.close()
            print("Created FilterMod File")
            await interaction.response.send_message("Filter is now turned on for this server.")
        else:
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