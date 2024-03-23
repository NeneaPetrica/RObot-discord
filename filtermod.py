

    class FliterMod(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self._last_member = None

        @commands.Cog.listener()
        async def on_message(message):
            if 'https://www.instagram.com/' in message.content.lower():
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on the server.')

    @commands.command()
        async def hello(self, ctx, *, member: discord.Member = None):
            """Says hello"""
            member = member or ctx.author
            if self._last_member is None or self._last_member.id != member.id:
                await ctx.send(f'Hello {member.name}~')
            else:
                await ctx.send(f'Hello {member.name}... This feels familiar.')
            self._last_member = member
