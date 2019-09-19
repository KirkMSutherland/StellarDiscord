# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from engine import Game

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

game = Game()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='register', help='Enters you into the game')
async def register(ctx):
    game.register_player(str(ctx.author))
    await ctx.send('{0} has joined the fray!'.format(ctx.author))

@bot.command(name='players', help='Shows everybody playing')
async def show_players(ctx):
    await ctx.send((game.get_players()))

@bot.command(name='resources', help='Shows your available resources')
async def show_resources(ctx):
    await ctx.send(game.get_resources(str(ctx.author)))

@bot.command(name='build', help='Construct something')
async def build_ship(ctx, type):
    await ctx.send(game.build_ship(str(ctx.author), type))

@bot.command(name='getfleet', help='Return your fleet status')
async def get_fleet(ctx):
    await ctx.send(game.get_fleet(str(ctx.author)))

bot.run(token)