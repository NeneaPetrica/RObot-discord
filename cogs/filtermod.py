from discord.ext import commands
import discord


class filtermod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Filter is ready")
    async def on_message(self, message: discord.Message, interaction: discord.Interaction):
        if 'https://www.instagram.com/' in message.content.lower():
            file = open(f"./bank/{interaction.guild.id}.txt", "r")
            temp_int = int(file.read())
            if temp_int == 1:
                await message.delete()
                await message.channel.send('FilterMod: Instagram posts are not allowed on this server.')
            else:
                print(f"Guild {interaction.guild.id} has filter turned off")
        await self.process_commands(message)


    @discord.app_commands.command(name = "togglefilter")
    async def togglefilter(self, interaction: discord.Interaction):
        """Toggles the filter setting"""
        file = open(f"./configs/{interaction.guild.id}-filter.txt", "r")
        temp_int = int(file.read())

        if temp_int == 0:
            file = open(f"../configs/{interaction.guild.id}-filter.txt", "w")
            file.write(str(1))
            file.close()
            await interaction.response.send_message("Filter is now turned on for this server.")
        else:
            file = open(f"../configs/{interaction.guild.id}-filter.txt", "w")
            file.write(str(0))
            file.close()
            await interaction.response.send_message("Filter is now turned on for this server.")


async def setup(bot):
    await bot.add_cog(filtermod(bot))