import discord
from discord.ext import commands 
import requests
import asyncio
import random

prefix = '!'
bot = commands.Bot(command_prefix=prefix, description='''Developed by: @DwarfThief#3805''', pm_help = True)

BOT_USER_TOKEN = "" #Put here your bot user token

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def btc(currency : str):
    """
    Usage: {command_prefix}btc ["COIN"]
    Price of Bitcoin
    """
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=' + currency
    response = requests.get(url)
    canned = response.json()
    await bot.say("1 BTC = " + str(canned[currency]) + " " + currency)
    print("1 BTC = " + str(canned[currency]) + " " + currency)


@bot.command()
async def eth(currency : str):
    """
    Usage: {command_prefix}eth ["COIN"]
    Price of Ethereum
    """
    url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=' + currency
    response = requests.get(url)
    canned = response.json()
    await bot.say("1 ETH = " + str(canned[currency]) + " " + currency)
    print("1 ETH = " + str(canned[currency]) + " " + currency)

@bot.command()
async def bch(currency : str):
    """
    Usage: {command_prefix}bch ["COIN"] 
    Price of Bitcoin Cash
    """
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=' + currency
    response = requests.get(url)
    canned = response.json()
    await bot.say("1 BCH = " + str(canned[currency]) + " " + currency)
    print("1 BCH = " + str(canned[currency]) + " " + currency)

bot.run(BOT_USER_TOKEN)
