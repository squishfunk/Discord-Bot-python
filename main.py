import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Njk0OTMwMDQ1NjQyMjExMzk4.XoSyCg.leIXE0H42Vf_YjoVCOoT5_5yZNA')