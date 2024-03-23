import discord
from discord.ext import commands

class ro_fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx, message: discord.Message, interaction: discord.Interaction):
        if 'bag pula' in message.content.lower():
            await ctx.send('Si eu sa mor!')

        if 'mario e gae' in message.content.lower():
            await ctx.send('Cel mai gaee')

        if 'sugi pula' in message.content.lower():
            await ctx.send('O sugi tu ma!')

        if 'la multi ani' in message.content.lower():
            await ctx.send('ADUCETI BAUTURAAAAAA!!!!')


async def setup(bot):
    await bot.add_cog(ro_fun(bot))