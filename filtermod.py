
class FliterMod_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(message):
        if 'https://www.instagram.com/' in message.content.lower():
            await message.delete()
            await message.channel.send('FilterMod: Instagram posts are not allowed on the server.')

