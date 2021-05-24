import discord
from discord.ext import commands
import asyncio

class Move(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def move(self, ctx, member: discord.Member=None, how_much=5):
        channel_name = 'AFK'
        nazwa = str(member.voice.channel)
        channel = discord.utils.get(ctx.guild.channels, name=nazwa)
        channelToMove = discord.utils.get(ctx.guild.channels, name=channel_name)

        print(member.voice.channel)



        for i in range(1,how_much):
            await member.move_to(channelToMove)
            await member.move_to(channel)

        await member.move_to(channel)


def setup(client):
    client.add_cog(Move(client))
