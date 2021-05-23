import discord
from discord.ext import commands
import youtube_dl
import os

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["p"])
    async def play(self, ctx, url : str):
        song_there = os.path.isfile('song.mp3')
        try:
            if song_there:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send('POCZEKAJ KURRRRRRRRRR')
            return

        #channel = ctx.message.author.voice.channel
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="BLACK CIRCLE 1")
        vc = await voiceChannel.connect()
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)



        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality' : '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith('.mp3'):
                os.rename(file, "song.mp3")
        vc.play(discord.FFmpegPCMAudio('song.mp3'))

    @commands.command(aliases=["l"])
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice != None:
            await voice.disconnect()
        else:
            await ctx.send("Nie jestem na żadnym kanale")

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send("Audio zapauzowane")
        else:
            await ctx.send("Nic nie gra.")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send("Play audio")
        else:
            await ctx.send("Audio nie jest zatrzymane")


def setup(client):
    client.add_cog(Music(client))