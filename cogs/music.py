import discord
from discord.ext import commands
import youtube_dl
import urllib.parse, urllib.request, re
import validators

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["p"])
    async def play(self, ctx, *, search):
        if ctx.author.voice is None:
            await ctx.send("Nie jesteś na kanale")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        if not validators.url(search):
            ##searching
            query_string = urllib.parse.urlencode({
                'search_query': search
            })
            htm_content = urllib.request.urlopen(
                'http://www.youtube.com/results?' + query_string
            )
            search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
            search = "http://www.youtube.com/watch?v=" + search_results[0]

        FFMPEG_OPTION = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                         'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        try:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(search, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTION)
                vc.play(source)
                await ctx.send('Teraz gram: ' + search)
        except:
            await ctx.send('Restrykcje wiekowe')

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