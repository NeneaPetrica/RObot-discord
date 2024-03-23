import discord
from discord.ext import commands
import random

class core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def writeHugs(user_id, hugs = int):
        file = open(f"./bank/{user_id}.txt", "r")
        temp_int = int(file.read())
        file = open(f"./bank/{user_id}.txt", "w")
        file.write(str(temp_int + hugs))
        file.close()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Core is ready")
    
    @commands.command()
    async def hello(interaction: discord.Interaction):
        """Says hi!"""
        await interaction.response.send_message(f"Hi, {interaction.user.mention}!")

    @commands.command()
    async def dice(interaction: discord.Interaction):
        """Rolls a dice"""
        await interaction.response.send_message(random.randint(1, 6))

    @commands.command()
    async def hug_register(interaction: discord.Interaction):
        """Register at the HugBank"""
        if os.path.isfile(f"./bank/{interaction.user.id}.txt"):
            await interaction.response.send_message("You are already registered with HugBank")
        else:
            file = open(f"./bank/{interaction.user.id}.txt", "a")
            file.write(str(100))
            file.close()
            await interaction.response.send_message("HugBank account opened with 100 hugs!")


    @commands.command()
    async def hug(interaction: discord.Interaction, hugged_user: discord.Member = None):
        """Give a hug to someone on the server"""
        file = open(f"./bank/{interaction.user.id}.txt", "r")
        temp_int = int(file.read())
        file = open(f"./bank/{interaction.user.id}.txt", "w")
        file.write(str(temp_int - 1))
        file.close()
        try:
            writeHugs(hugged_user.id, 1)
        except:
            await interaction.response.send_message("The hugged user does not have a HugBank Account! :(")

        await interaction.response.send_message(f"{interaction.user.mention} hugged <@{hugged_user.id}>!"
                                                "\n"
                                                "https://imgur.com/gallery/V6HmXVi")

    @commands.command()
    async def balance(interaction: discord.Interaction):
        """See the hug balance"""
        file = open(f"./bank/{interaction.user.id}.txt", "r")
        temp_int = int(file.read())
        file.close()
        await interaction.response.send_message(f"You have {temp_int} hugs!")

    @commands.command()
    async def slotmachine(interaction: discord.Interaction):
        """Get more slots from gambling!"""
        emoteArray = []

        for i in range(3):
            temp_val = random.randint(1,4)

            if(temp_val == 1):
                temp_emote = ":grapes:"
            elif(temp_val == 2):
                temp_emote = ":cherries:"
            elif (temp_val == 3):
                temp_emote = ":strawberry:"
            else:
                temp_emote = ":watermelon:"
            
            emoteArray.append(temp_emote)
            
        emote1 = str(emoteArray[0])
        emote2 = str(emoteArray[1])
        emote3 = str(emoteArray[2])

        if (emote1 == ":grapes:" and emote2 == ":grapes:" and emote3 == ":grapes:"):
            writeHugs(interaction.user.id, 500)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 500 hugs!")

        elif (emote1 == ":cherries:" and emote2 == ":cherries:" and emote3 == ":cherries:"):
            writeHugs(interaction.user.id, 1000)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 1000 hugs!")

        elif (emote1 == ":strawberry:" and emote2 == ":strawberry:" and emote3 == ":strawberry:"):
            writeHugs(interaction.user.id, 1250)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 1250 hugs!")

        elif (emote1 == ":watermelon:" and emote2 == ":watermelon:" and emote3 == ":watermelon:"):
            writeHugs(interaction.user.id, 100000)
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n You won 100,000 hugs! JACKPOT!")
        else:
            await interaction.response.send_message(f">{emoteArray[0]}|{emoteArray[1]}|{emoteArray[2]}<\n Better luck next time!")

    @commands.command()
    async def all_in(interaction: discord.Interaction):
        """Double or nothing!"""
        temp_val = random.randint(1,100)
        if temp_val == 1:
            file = open(f"./bank/{interaction.user.id}.txt", "r")
            temp_int = int(file.read())
            file = open(f"./bank/{interaction.user.id}.txt", "w")
            file.write(str(temp_int * 2))
            file.close()
            await interaction.response.send_message("You've doubled your Hugs!!! Really lucky!")
        else:
            file = open(f"./bank/{interaction.user.id}.txt", "r")
            temp_int = int(file.read())
            file = open(f"./bank/{interaction.user.id}.txt", "w")
            file.write(str(0))
            file.close()
            await interaction.response.send_message("You've lost all hugs. T-T")

    @commands.command()
    async def register_quotebook(interaction: discord.Interaction):
        """Makes a server quotebook"""
        quotes_file = open(f'./quotes/{interaction.guild.id}-quotes.txt', 'w')
        await interaction.response.send_message("A quotebook for the server has been created.")


    @commands.command()
    async def quote(interaction: discord.Interaction):
        """Says a quote"""
        try:
            quotes_file = open(f"./quotes/{interaction.guild.id}-quotes.txt", 'r')
            quotes = quotes_file.readlines()
            temp_quotes = []
            response = random.choice(quotes)
            await interaction.response.send_message(response)
        except:
            await interaction.response.send_message("Your server does not have a quote book. To create one use the command: /register_quotebook")


    @commands.command()
    async def add_quote(interaction: discord.Interaction, new_quote: str):
        """Adds a quote to the quotebook"""
        quotes_file = open(f"./quotes/{interaction.guild.id}-quotes.txt", 'a')
        quotes_file.write(new_quote)

        await interaction.response.send_message(f"You added the quote: {new_quote}")

    @commands.command()
    async def help(interaction: discord.Interaction):
        """Tells what AstroBot can do"""
        await interaction.response.send_message(
                "```Hi, my name is AstroBot! I am here to make your day a bit better!\n"
                "This is what I can do:\n \n"

                "\n ==== Small Commands ====\n"
                "/hello - Says hi to you :)\n"
                "/dice - Roll a dice\n"
                
                "\n ==== Quote books ====\n"
                "/register-quotebook - Makes a special quotebook for the server \n"
                "/add_quote {new_quote} - Adds a quote to the server quotebook \n"
                "/quote - Says a random quote from the server quotebook \n"
                
                "\n ==== HugBank ====\n"
                "/hug_register - Registers you to HugBank\n"
                "/hug {tag a user} - Sends a hug to the hugged user\n"
                "/balance - See the hug balance\n"

                "\n ==== Gambling ====\n"
                "/slotmachine - You play slots and can win Hugs!\n \n"

                "Slots Prizes: \n"
                ">🍇|🍇|🍇< for 500 hugs\n"
                ">🍒|🍒|🍒< for 1000 hugs\n"
                ">🍓|🍓|🍓< for 1250 hugs\n"
                ">🍉|🍉|🍉< for the JACKPOT (which is secret)\n \n"

                "/all_in - Doubles your Hugs or lose them all.\n"
                "\n```")

async def setup(bot):
    await bot.add_cog(core(bot))


    