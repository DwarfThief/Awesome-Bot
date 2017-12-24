import discord
from discord.ext import commands 
import requests

client = commands.Bot(command_prefix='!', description='''Developed by: @DwarfThief#3805''', pm_help = True)

BOT_USER_TOKEN = " " #<- Put here your token

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def coin(compare1 : str, compare2 : str):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={compare1}&tsyms={compare2}'
    response = requests.get(url)
    canned = response.json()
    await client.say(str(canned[compare2]))



client.run(BOT_USER_TOKEN)
