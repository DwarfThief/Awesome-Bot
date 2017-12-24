import discord
from discord.ext import commands
from discord.ext.commmands import Bot  
import requests

client = Bot(command_prefix='!', description='''Developed by: @DwarfThief#3805''', pm_help = True)

BOT_USER_TOKEN = "Mzk0MzMxNzQwODM2OTg2ODgw.DSC23A.gk7Zje-wFWLPJq3OtvmUzJl51Vc"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def btc(currency : str):
    url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=' + currency
    response = requests.get(url)
    btc = respose.json()[currency]
    await client.say(str(btc['24h_volume_'+currency]))


client.run(BOT_USER_TOKEN)
