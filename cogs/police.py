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
        if interaction.user.guild_permissions.manage_messages == True:
            await interaction.response.defer()
            deleted = await interaction.channel.purge(limit=messages + 1, bulk= True)
            await interaction.channel.send(f'Deleted {len(deleted)} message(s)')
        else:
            await interaction.response.send_message("You don't have the following permission: manage_messages.")
    


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(police(bot))