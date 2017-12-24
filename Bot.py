import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix='!', description='''Developed by: @DwarfThief#3805''', pm_help = True)

BOT_USER_TOKEN = " " #<--add here your bot_token

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
