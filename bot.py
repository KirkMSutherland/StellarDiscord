# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

import discord

from engine import Game

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

client = discord.Client()

game = Game()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='register', help='Enters you into the game')
async def register(ctx):
    game.register_player(str(ctx.author))
    await ctx.send('{0} has joined the fray!'.format(ctx.author))

@bot.command(name='players', help='Shows everybody playing')
async def show_players(ctx):
    await ctx.send((game.get_players()))

bot.run(token)
client.run(token)