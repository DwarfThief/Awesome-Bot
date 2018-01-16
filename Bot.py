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

@bot.command()
async def D4(times:int):
    """
    Usage: {command_prefix}D4 [times]
    Roll a D4 many time as you want
    """

    for x in range(times):
        await bot.say(str(random.randint(1, 4)) + " :game_die:")
    
@bot.command()
async def D6(times:int):
    """
    Usage: {command_prefix}D6 [times]
    Roll a D6 many time as you want
    """

    for x in range(times):
        await bot.say(str(random.randint(1, 6)) + " :game_die:")

@bot.command()
async def D8(times:int):
    """
    Usage: {command_prefix}D8 [times]
    Roll a D8 many time as you want
    """

    for x in range(times):
        await bot.say(str(random.randint(1, 8)) + " :game_die:")

@bot.command()
async def D10(times:int):
    """
    Usage: {command_prefix}D10 [times]
    Roll a D10 many time as you want
    """

    for x in range(times):
        await bot.say(str(random.randint(1, 10)) + " :game_die:")

@bot.command()
async def D12(times:int):
    """
    Usage: {command_prefix}D12 [times]
    Roll a D12 many time as you want
    """

    for x in range(times):
        await bot.say(str(random.randint(1, 12)) + " :game_die:")

@bot.command()
async def D20(times:int):
    """
    Usage: {command_prefix}D20 [times]
    Roll a D20 many time as you want
    """

    for x in range(times):
        await bot.say(str(random.randint(1, 20)) + " :game_die:")

bot.run(BOT_USER_TOKEN)
