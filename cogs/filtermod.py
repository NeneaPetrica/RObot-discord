import discord
from discord.ext import commands

class filtermod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Filter is ready")



    @commands.command()
    async def filtermod(self, ctx, *, member: discord.Member = None):
        """Toggles the filter setting"""
        file = open(f"./configs/{ctx.guild.id}-filter.txt", "r")
        temp_int = int(file.read())

        if temp_int == 0:
            file = open(f"../configs/{ctx.guild.id}-filter.txt", "w")
            file.write(str(1))
            file.close()
            await ctx.send("Filter is now turned on for this server.")
        else:
            file = open(f"../configs/{ctx.guild.id}-filter.txt", "w")
            file.write(str(0))
            file.close()
            await ctx.send("Filter is now turned on for this server.")


async def setup(bot):
    await bot.add_cog(filtermod(bot))