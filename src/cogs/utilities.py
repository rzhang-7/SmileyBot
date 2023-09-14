import discord
import asyncio
import math
from discord.ext import commands

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands

    @commands.command(aliases=['!'])
    async def factorial(self, ctx, num):
        answer = math.factorial(int(num))
        await ctx.send(answer)

    @commands.command(aliases=['factor'])
    async def factors(self, ctx, num):
        if num == '0':
            await ctx.send("∞")
            return
        counter = 1
        factors = 0
        factorList = []
        for counter in range(1, int(num)):
            if int(num) % counter == 0:
                factorList.append(counter)
                factors += 1
            if int(num) % counter > 0:
                continue
            if counter == int(num)//2:
                break
            counter += 1
        factorList.append(int(num))  # Because num wasn't counted   
        factors += 1  
        factorList = str(factorList)[1:len(str(factorList))-1]
        await ctx.send(f"{num} has {factors} factor(s): \n**{factorList}**")

    @commands.command()
    async def pfactor(self, ctx, num):
        if num == '0':       
            await ctx.send("∞")
            return
        if num == '1':
            await ctx.send('`Math error: 1 is not prime nor composite`')
            return
        
        i = 2
        factors = []
        intnum = int(num)
        while i * i <= intnum:
            if intnum % i:
                i += 1
            else:
                intnum //= i
                factors.append(i)
        if intnum  > 1:
            factors.append(intnum)

        factors = str(factors)[1:len(str(factors))-1]
        multiplyFactors = factors.replace(',', ' ⋅')

        if len(multiplyFactors) == len(num):  
            await ctx.send(f"{num} is a prime number")
            return

        await ctx.send(f"{num} = **{str(multiplyFactors)}**")

    @commands.command(aliases=['f'])
    async def fahrenheit(self, ctx, celcius):
        await ctx.send(f'🌡 | {celcius}°C ≈ **{round(int(celcius)*9/5 + 32, 1)}°F**')

    @commands.command(aliases=['c'])
    async def celcius(self, ctx, fahrenheit):
        await ctx.send(f"🌡 | {fahrenheit}°F ≈ **{round((int(fahrenheit)-32)*5/9, 1)}°C**")

    @commands.command()
    async def pi(self, ctx, digits=None):
        pi = math.pi
        if digits == None:
            await ctx.send(pi)
            return
        digits = int(digits) 
        await ctx.send(round(pi, digits))
# do later    
#    @commands.command()
#    async def remindme(self, ctx, *, reminder, days=None, hours=None, minutes=None, seconds=None)


    # Errors

    @factorial.error
    async def factorial_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an integer. If you were looking for the value of 0!, do `s.factorial 0` pLeAsE and go to `s.help util` pLeAsE')

    @factors.error
    async def factors_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Hopefully you just forgot to specify a number. If you were just screwing with me and you keep this up... you're gonna have a bad time.")
            await ctx.send("Go to `s.help util` for help if you're ~~braindead~~ stuck plzkthxbye")

    @pfactor.error
    async def pfactor_error(self, ctx, error):
        flowey_angy = '<:flowey_angy:729714435148480553>'
        flowey_whoops = '<:flowey_whoops:729720922252247051>'
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{flowey_angy} Is this a Joke? Are you Braindead? SPECIFY. A. ~~SACRIFICE!!!~~ number')
            await ctx.send(f"{flowey_whoops} Try going to `s.help util` for help?")

def setup(client):
    client.add_cog(Utilities(client))