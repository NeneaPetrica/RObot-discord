import discord
from discord.ext import commands

class ro_fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if 'bag pula' in message.content.lower():
            await message.channel.send('Si eu sa mor!')

        if 'mario e gae' in message.content.lower():
            await message.channel.send('Cel mai gaee')

        if 'sugi pula' in message.content.lower():
            await message.channel.send('O sugi tu ma!')

        if 'la multi ani' in message.content.lower():
            await message.channel.send('ADUCETI BAUTURAAAAAA!!!!')
        await self.process_commands(message)


async def setup(bot):
    await bot.add_cog(ro_fun(bot))