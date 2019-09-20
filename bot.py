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

@bot.command(name='register', help='Enters you into the game', aliases=['reg'])
async def register(ctx):
    game.register_player(str(ctx.author))
    await ctx.send('{0.mention} has joined the fray!'.format(ctx.author))

@bot.command(name='players', help='Shows everybody playing')
async def show_players(ctx):
    await ctx.send((game.get_players()))

@bot.command(name='resources', help='(rs) Shows your available resources', aliases=['rs'])
async def show_resources(ctx):
    await ctx.send(game.get_resources(str(ctx.author)))

@bot.command(name='buildship', help='(bs) Build a ship in your shipyard', aliases=['bs'])
async def build_ship(ctx, type):
    await ctx.send('{0.mention}'.format(ctx.author) + game.build_ship(str(ctx.author), type))

@bot.command(name='buildzone', help='(bz) Develop an economic zone', aliases=['bz'])
async def build_zone(ctx, planet, zone_type):
    await ctx.send('{0.mention}'.format(ctx.author) + game.build_zone(str(ctx.author), planet, zone_type))

@bot.command(name='getfleet', help='(gf) Return your fleet status', aliases=['gf'])
async def get_fleet(ctx):
    await ctx.send(game.get_fleet(str(ctx.author)))

@bot.command(name='claimplanet', help='(clp) Claim a planet', aliases=['clp'])
async def claim_planet(ctx, planet_name):
    await ctx.send('{0.mention}'.format(ctx.author) + game.claim_planet(str(ctx.author), planet_name))

bot.run(token)