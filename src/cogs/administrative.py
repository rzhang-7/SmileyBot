import discord
import asyncio
from discord.ext import commands

class Administrative(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    #nothing here... yet
     
    # Commands
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if member == ctx.message.author:
            await ctx.send('You know leaving the server is a thing, right?')
            return
        if reason == None:
            reason = '😳'
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been given the boot  :boot:')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if member == ctx.message.author:
            await ctx.send('Seems like you really wanna break ties with this server...')
            return
        if reason == None:
            reason = '😳'
        message = f"You will no longer be able to join {ctx.guild.name} until further notice"
        await message.send(message)    
        await member.ban(reason=reason)
        await ctx.send(f'The ban hammer has been swung on {member.mention}  :hammer:')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        if member == ctx.message.author:
            await ctx.send("You can't be sending this if you're banned. Maybe someone can help with that")
            return
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        ubmessage = f'You have been unbanned from {ctx.guild.name}. Enjoy'

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'The ban hammer has been lifted from {user.mention}')
                await ubmessage.send(ubmessage)
                return

        

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member=None, reason=None):
        if member == ctx.message.author:
            await ctx.send("What are you trying to achieve by doing this?")
            return
        if reason == None:
            reason = '😳'
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.name} has muted {member.mention} via duck tape :duck:" )

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member:discord.Member=None, reason=None):
        if member == ctx.message.author:
            await ctx.send("My disappointment is immeasurable and my day is ruined")
            return
        if reason == None:
            reason = '😳'
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(f"{ctx.author.name} has ripped the duck tape off {member.mention} :duck:" )
    
    @commands.command(aliases=['prune', 'purge', 'delete'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount+1)

    # Errors

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please mention someone to kick')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the power to use this command')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please mention someone to banish via ban hammer')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('This power... it is too strong for you')    

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify a tag to unbanish')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sadly, you cannot be nice and unban people at your current state :<')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('The owner does not entrust you with this power')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to erase from this world')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Silence is golden, \nDuck tape is silver, \nNothing rhymes with silver, \nPlease specify a user")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('This brand of duck tape can only be applied with admin hands and is too dangerous for a normie like you >:>')

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bots have feelings, \nI wonder who'll be unmuted, \nBut that wasn't stated, \nSo it's still disputed" )
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("This tape is too sticky for you to remove...")
def setup(client):
    client.add_cog(Administrative(client))