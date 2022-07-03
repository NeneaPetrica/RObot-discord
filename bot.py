import discord, random
from discord.ext import commands 

config = {
        "token": "token-here",
        "language": ""
}

transl = {
        "help":  {
                "description": "Displays the help menu",
                "alt_name": "ajutor",
                "alt_description": "Afiseaza meniul de ajutor",
        },
        "dice":  {
                "description": "Roll a dice, try your luck",
                "alt_name": "zar",
                "alt_description": "Pentru a da cu zarul",
        },
        "quote": {
                "description": "Say one of the quotes from my little book",
                "alt_name": "fraza",
                "alt_description": "O sa deschid carticica cu replici amuzante si o sa spun una"
        }
}

config["language"] = str(input("Language [!en/ro]: "))
lang = config["language"]

client = commands.Bot(command_prefix='$')
client.remove_command('help')

def checkCmdLang(param):

        if lang == "ro":
                c = {
                        "name": transl[f"{param}"]["alt_name"],
                        "description": transl[f"{param}"]["alt_description"],
                        "usage": client.command_prefix + transl[f"{param}"]["alt_name"]
                }

        else:
                c = {
                        "name": param,
                        "description": transl[f"{param}"]["description"],
                        "usage":  client.command_prefix + param
                }

        return c

@client.event
async def on_ready():
        print("Bot has connected to Discord")
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="", type=3))

@client.command(name = checkCmdLang("help")["name"], description = checkCmdLang("help")["description"], usage = checkCmdLang("help")["usage"]) 
async def help(ctx):
        commandsList = ""
        for i in client.commands:
                commandsList += f"[/] {i.name} » {i.description} » {i.usage}\n"

        if lang == "ro":
                await ctx.send(f'''
```
Sunt noul tau ajutor!  
[>] Nume » Descriere  » Utilizare
-------------------------------------------------------->
{commandsList}
```''')
        else: 
                await ctx.send(f'''
```
Hi! I am here to make your day a bit better!
-------------------------------------------------------->
[>] Name » Description » Usage
{commandsList}
```
''')
      
@client.command(name = checkCmdLang("dice")["name"], description = checkCmdLang("dice")["description"], usage = checkCmdLang("dice")["usage"]) 
async def dice(ctx):
        await ctx.send(random.randint(1,6))

@client.command(name = checkCmdLang("quote")["name"], description = checkCmdLang("quote")["description"], usage = checkCmdLang("quote")["usage"]) 
async def quote(ctx):

        quotes_file = open('quotes.txt','r')
        quotes = quotes_file.readlines()

        quote = random.choice(quotes)
        await ctx.send(quote)

client.run(config["token"])

#i used google translate, aint romanian
