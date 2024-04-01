import discord
from discord.ext import commands
from discord import app_commands

class police(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready():
       await print("Loading police.py...")

    @app_commands.command(name = "delete", description="Deletes messages")
    async def delete(self, interaction: discord.Interaction, messages: int):
        if interaction.user.guild_permissions.manage_guild == True:
            await interaction.response.defer()
            deleted = await interaction.channel.purge(limit=messages, bulk= True)
            await interaction.channel.send(f'Deleted {len(deleted)} message(s)')
        else:
            await interaction.channel.send("You don't have the following permission: manage_guild.")
    


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(police(bot))