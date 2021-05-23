import discord
from discord.ext import commands

class Init(commands.Cog):

    def __init__(self, client):
        self.client = client

    # EVENTS
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('World of Warcraft'))
        print('Bot is online')


def setup(client):
    client.add_cog(Init(client))