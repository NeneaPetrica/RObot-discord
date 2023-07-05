import os
import discord
from discord import app_commands
from discord.ext import commands
import random

token_file = open("token.txt", "r")
TOKEN = str(token_file.read())
token_file.close()

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():

    print("Bot has connected to Discord")
    activity = discord.Game(name="/help", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)!")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello", description="Says hi!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi, {interaction.user.mention}!")


@bot.tree.command(name="dice", description="Rolls a dice")
async def dice(interaction: discord.Interaction):
    await interaction.response.send_message(random.randint(1, 6))


@bot.tree.command(name="hug_register", description="Register at the HugBank")
async def hug_register(interaction: discord.Interaction):
    if os.path.isfile(f"./bank/{interaction.user.id}.txt"):
        await interaction.response.send_message("You are already registered with HugBank")
    else:
        file = open(f"./bank/{interaction.user.id}.txt", "a")
        file.write(str(100))
        file.close()
        await interaction.response.send_message("HugBank account opened with 100 hugs!")


@bot.tree.command(name="hug", description="Give a hug to someone on the server")
async def hug(interaction: discord.Interaction, hugged_user: str):
    file = open(f"./bank/{interaction.user.id}.txt", "r")
    temp_int = int(file.read())
    file = open(f"./bank/{interaction.user.id}.txt", "w")
    file.write(str(temp_int - 1))
    file.close()

    await interaction.response.send_message(f"{interaction.user.mention} hugged {hugged_user}!"
                                            "\n"
                                            "https://imgur.com/gallery/V6HmXVi")


@bot.tree.command(name="balance", description="See the hug balance")
async def balance(interaction: discord.Interaction):
    file = open(f"./bank/{interaction.user.id}.txt", "r")
    temp_int = int(file.read())
    file.close()
    await interaction.response.send_message(f"You have {temp_int} hugs!")


@bot.tree.command(name="register_quotebook", description="Makes a server quotebook")
async def register_quotebook(interaction: discord.Interaction):
    quotes_file = open(f'./quotes/{interaction.guild.id}-quotes.txt', 'w')
    await interaction.response.send_message("A quotebook for the server has been created.")


@bot.tree.command(name="quote", description="Says a quote")
async def quote(interaction: discord.Interaction):
    try:
        quotes_file = open(f"./quotes/{interaction.guild.id}-quotes.txt", 'r')
        quotes = quotes_file.readlines()
        temp_quotes = []
        response = random.choice(quotes)
        await interaction.response.send_message(response)
    except:
        await interaction.response.send_message("Your server does not have a quote book. To create one use the command: /register_quotebook")


@bot.tree.command(name="add_quote", description="Adds a quote to the quotebook")
async def add_quote(interaction: discord.Interaction, new_quote: str):
    quotes_file = open(f"./quotes/{interaction.guild.id}-quotes.txt", 'a')
    quotes_file.write(new_quote)

    await interaction.response.send_message(f"You added the quote: {new_quote}")


@bot.tree.command(name="help", description="Tells what AstroBot can do")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
            "```Hi! I am here to make your day a bit better!\n"
            "This is what I can do:\n"
            
            "\n /hello - Says hi to you :)\n"
            "/dice - Roll a dice\n"
            
            "\n ==== Quote books ====\n"
            "/register_quotebook - Makes a special quotebook for the server \n"
            "/add_quote {new_quote} - Adds a quote to the server quotebook \n"
            "/quote - Says a random quote from the server quotebook \n"
            
            "\n ==== HugBank ====\n"
            "/hug_register - Registers you to HugBank\n"
            "/hug {tag a user} - Sends a hug to the hugged user\n"
            "/balance - See the hug balance\n"
            "\n```")


@bot.event
async def on_message(message):

    if 'bag pula' in message.content.lower():
        await message.channel.send('Si eu sa mor!')

    if 'mario e gae' in message.content.lower():
        await message.channel.send('Cel mai gaee')

    if 'sugi pula' in message.content.lower():
        await message.channel.send('O sugi tu ma!')

    if 'la multi ani' in message.content.lower():
        await message.channel.send('ADUCETI BAUTURAAAAAA!!!!')

bot.run(TOKEN)
