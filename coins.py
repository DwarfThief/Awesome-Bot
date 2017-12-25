import discord
from discord.ext import commands 
import requests

bot = commands.Bot(command_prefix='!', description='''Developed by: @DwarfThief#3805''', pm_help = True)

class CoinsSearch(object):
	
	@bot.command()
	async def btc(currency : str):
	    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=' + currency
	    response = requests.get(url)
	    canned = response.json()
	    await bot.say("1 BTC = " + str(canned[currency]) + " " + currency)
	    print("1 BTC = " + str(canned[currency]) + " " + currency)
	@bot.command()
	async def eth(currency : str):
	    url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=' + currency
	    response = requests.get(url)
	    canned = response.json()
	    await bot.say("1 ETH = " + str(canned[currency]) + " " + currency)
	    print("1 ETH = " + str(canned[currency]) + " " + currency)
	@bot.command()
	async def bch(currency : str):
	    url = 'https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=' + currency
	    response = requests.get(url)
	    canned = response.json()
	    await bot.say("1 BCH = " + str(canned[currency]) + " " + currency)
	    print("1 BCH = " + str(canned[currency]) + " " + currency)
