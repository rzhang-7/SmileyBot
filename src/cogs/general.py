import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    # Commands


def setup(client):
    client.add_cog(General(client))