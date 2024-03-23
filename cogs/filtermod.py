import discord
from discord import app_commands
from discord.ext import commands
from discord import *
from discord.ext.commands import has_permissions

class filtermod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message, interaction: discord.Interaction):
        if 'https://www.instagram.com/' in message.content.lower():
            file = open(f"./bank/{interaction.guild.id}.txt", "r")
            temp_int = int(file.read())
            if temp_int == 1:
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            else:
                await print(f"Guild {interaction.guild.id} has filter turned off")

    @commands.command()
    async def toggle_filter(self, ctx):
            """Toggles the filter setting"""
            await discord.Message.channel.send("Test")

async def setup(bot):
    await bot.add_cog(filtermod(bot))