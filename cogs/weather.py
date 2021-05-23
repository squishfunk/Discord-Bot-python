import discord
from discord.ext import commands
import json
import requests


def get_info(city):
    response = requests.get(f"https://danepubliczne.imgw.pl/api/data/synop/station/{city}")
    json_data = json.loads(response.text)
    #info = json_data['temperatura'] + " stopni w: " + json_data['stacja']
    info = discord.Embed(title=json_data['stacja'], color=0x00ff00 )
    info.add_field(name="Temperatura: ", value=json_data['temperatura'] + "º", inline=False)
    info.add_field(name="Cisnienie: ", value=json_data['cisnienie'], inline=False)
    info.add_field(name="Godzina pomiaru: ", value=json_data['godzina_pomiaru'] + ":00", inline=False)

    return(info)

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    # LISTENER
    @commands.Cog.listener()
    async def test1(self):
        return

    # COMMANDS
    @commands.command(aliases=["pogoda"])

    async def pog(self, ctx, city='bialystok'):

        await ctx.send(embed=get_info(city))


def setup(client):
    client.add_cog(Weather(client))