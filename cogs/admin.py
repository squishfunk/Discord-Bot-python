import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["c"])
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)


def setup(client):
    client.add_cog(Admin(client))