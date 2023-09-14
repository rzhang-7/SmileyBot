import discord
import random
import asyncio
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    # Commands

    @commands.command(aliases=['ritual', 'mingchange', 'satanicritual'])
    async def summon(self, ctx, *, member):
        if member == 'Smiley':
            await ctx.send("You can't summon me; I'm already here")
        await ctx.send('**                 **:candle:\n         :candle: :duck: :candle:\n**             **:candle:  :candle:')
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)
        await ctx.send('**         **:fire: :fire: :fire:\n**   **:fire:       :candle:       :fire:\n** **:fire:  :candle: :duck: :candle:  :fire:\n**   **:fire:   :candle:  :candle:   :fire:\n**          **:fire: :fire: :fire:')
        await ctx.send(f'`{ctx.member.mention} has awoken!`')

    @commands.command()
    async def temmie(self, ctx):
        await ctx.send("hOI!! i'm tEMMIE!!")
        await ctx.send('░░░░░░░░░░▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░██▀█▄░░▄██▀░░░░▄██▄░░░░░░░░░░░\n░░░░░░░░██▄▄▄████████▄▄█▀░▀█░░░░░░░░░░░\n░░░░░░░▄██████████████████▄█░░░░░░░░░░░\n░░░░░░▄██████████████████████░░░░░░░░░░\n░░░░░▄████████▀░▀█████████████░░░░░░░░░\n░░░░░███████▀░░░░▀████████████▄░░░░░░░░\n░░░░██████▀░░░░░░░░▀███████████▄▄▄▀▀▄░░\n░▄▀▀████▀░░░▄▄░░░░░░░░░████████░░░░░█░░\n█░░░▀█▀█░░░░▀▀░░░░░░██░░███░██▀░░░░▄▀░░\n█░░░░▀██▄░░░▄░░░▀░░░▄░░░███░██▄▄▄▀▀░░░░\n░▀▄▄▄▄███▄░░▀▄▄▄▀▄▄▄▀░░░███░█░░░░░░░░░░\n░░░░░░████▄░░░░░░░░░░░░▄██░█░░░░░░░░▄▀▀\n░░░░░░███▀▀█▀▄▄▄▄▄▄▄▄▄▀█████░░░░░░▄▀░░▄\n░░░░░░█▀░░█░▀▄▄▄▄▄▄▄▄▄▀░███░█▀▀▀▄▀░░▄▀░\n░░░░░░░░░▄▀░░░░░░░░░░░░░▀█▀░░█░░░░█▀░░░\n░░░░░░░░░█░░░█░░░░░░░░░░░░░░░█░░░░░█░░░\n░░░░░░░░░█▄▄█░▀▄░░█▄░░░░░░░░█░░▄█░░█░░░\n░░░░░░░░░▀▄▄▀░░█▀▀█░▀▀▀▀█▀▀█▀▀▀▀█░█░░░░')
  
    @commands.command(aliases=['cf', 'coin', 'flip'])
    async def coinflip(self, ctx, guess):
        coinFace = ['heads', 'tails']
        if guess == 'h':
            guess = 'heads'
        if guess == 't':
            guess = 'tails'
        outcome = random.choice(coinFace)
        if guess == outcome:
            await ctx.send(f'...{outcome}! Congrats! You won nothing!')
            await ctx.send('`Self-esteem +1`\n`Unluckiness -1`\n`Morale +1`')
        elif guess != outcome:
            await ctx.send(f"...{outcome}! Congrats! You're wrong!")
            await ctx.send('`Self-esteem -1`\n`Unluckiness +1`\n`Stupidity +1`')
    
    @commands.command()
    async def roll(self, ctx, sides):  # Add an option for multiple rolls
        if sides[0] == 'd':            # Make so that it will ignore the 'd' (e.g., s.roll d20)
            sides = sides[1:len(sides)-1]
        await ctx.send(f"🎲 **{ctx.author.name}** rolled a **__{str(random.randint(1, int(sides)))}__** from a d{sides}")
    
    # Errors

    @summon.error
    async def summon_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention someone to summon via ~~ping~~ satanic ritual")
            await ctx.send('Refer to `s.help fun` if you want to do it properly :knife:')

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You're not the one flipping the coin here, so you have to guess")
            await ctx.send("If you're that much of an unintellectual, go to `s.help fun` for assistance")

def setup(client):
    client.add_cog(Fun(client))