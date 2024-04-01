import os
import discord
from discord.ext import commands
import random
import asyncio
from multiprocessing import Pool
import subprocess

token_file = open("token.txt", "r")
TOKEN = str(token_file.read())
token_file.close()

intents=discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all(), help_command= None)

def writeHugs(user_id, hugs = int):
    file = open(f"./bank/{user_id}.txt", "r")
    temp_int = int(file.read())
    file = open(f"./bank/{user_id}.txt", "w")
    file.write(str(temp_int + hugs))
    file.close()


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def reload():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.reload_extension(f"cogs.{filename[:-3]}")
        
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

@bot.tree.command(name = "reload", description= "reloads bot")
async def reload(interaction: discord.Interaction):
    subprocess.run(["git pull"])
    await interaction.response.defer()
    await reload()
    await interaction.response.send_message("bot reloaded")

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
async def hug(interaction: discord.Interaction, hugged_user: discord.Member = None):
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


@bot.tree.command(name="balance", description="See the hug balance")
async def balance(interaction: discord.Interaction):
    file = open(f"./bank/{interaction.user.id}.txt", "r")
    temp_int = int(file.read())
    file.close()
    await interaction.response.send_message(f"You have {temp_int} hugs!")

@bot.tree.command(name="slotmachine", description="Get more hugs from gambling!")
async def slotmachine(interaction: discord.Interaction):
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

@bot.tree.command(name="all_in", description="Double or nothing!")
async def all_in(interaction: discord.Interaction):
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

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())


