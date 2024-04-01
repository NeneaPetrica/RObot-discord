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
    @app_commands.checks.has_permissions(manage_guild = True)
    async def delete(self, interaction: discord.Interaction, messages: int):
        deleted = interaction.channel.purge(limit=messages)
        try:
            await interaction.response.send_message(f'Deleted {messages} message(s)')
        except:
            await interaction.response.send_message(f'Deleted {len(deleted)} message(s)')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(police(bot))