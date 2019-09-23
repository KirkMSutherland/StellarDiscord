# bot.py
import os
import discord

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
    game.register_player(ctx.author.id)
    await ctx.send('{0.mention} has joined the fray!'.format(ctx.author))


@bot.command(name='players', help='Shows everybody playing')
async def show_players(ctx):
    await ctx.send((game.get_players()))


@bot.command(name='resources', help='(rs) Shows your available resources', aliases=['rs'])
async def show_resources(ctx):
    await ctx.send(game.get_resources(ctx.author.id))


@bot.command(name='buildship', help='(bs) Build a ship in your shipyard', aliases=['bs'])
async def build_ship(ctx, type):
    await ctx.send('{0.mention}'.format(ctx.author) + game.build_ship(ctx.author.id, type.upper()))


@bot.command(name='buildzone', help='(bz) Develop an economic zone', aliases=['bz'])
async def build_zone(ctx, planet, zone_type):
    await ctx.send('{0.mention}'.format(ctx.author) + game.build_zone(ctx.author.id, planet, zone_type.upper()))


@bot.command(name='getfleet', help='(gf) Return your fleet status', aliases=['gf'])
async def get_fleet(ctx):
    await ctx.send(game.get_fleet(ctx.author.id))


@bot.command(name='getzones', help='(gz) Lists economic zones on a planet', aliases=['gz'])
async def get_zones(ctx, planet_name):
    await ctx.send(game.get_zones(ctx.author.id, planet_name))


@bot.command(name='claimplanet', help='(clp) Claim a planet', aliases=['clp'])
async def claim_planet(ctx, planet_name):
    await ctx.send('{0.mention}'.format(ctx.author) + game.claim_planet(ctx.author.id, planet_name))


@bot.command(name='produce', help='(pd) Have a special zone produce goods', aliases=['pd'])
async def produce(ctx, zone_name):
    await ctx.send('{0.mention}'.format(ctx.author) + game.produce(ctx.author.id, zone_name))


@bot.command(name='empire', help='(emp) Returns the status of your overall Empire', aliases=['emp'])
async def empire(ctx):
    await ctx.send('Glory to the {0.mention}'.format(ctx.author) + ' Empire!\n' + game.empire(ctx.author.id))


@bot.command(name='trade', help='(td) Propose a trade between two players', aliases=['td'])
async def trade(ctx, *args):
    msg = game.propose_trade(ctx.author, ctx.message.mentions[0].id, args)
    if msg is False:
        await ctx.send('Trade recinded')
        for n in bot.cached_messages:
            if n.id == game.trades[args[0]].msgid:
                await n.delete()
                del game.trades[args[0]]
                break
    else:
        post = await ctx.send(msg)
        game.add_tradeid(args[0], post.id)
        await post.add_reaction('\U0001f44d')
        await post.add_reaction('\U0001f44e')


@bot.event
async def on_reaction_add(reaction, user):
    print('{0} {1}'.format(reaction.message.id, user.id))

    # ignore self
    if user == bot.user:
        return

    # check trades
    for n in game.trades:
        if game.trades[n].msgid == reaction.message.id:
            if user.id == game.trades[n].partner:
                if reaction.emoji == '\U0001f44d':
                    msg = game.complete_trade(n)
                    print(msg)
                elif reaction.emoji == '\U0001f44e':
                    print("don't trade!")


bot.run(token)
