import discord
from discord.ext import commands
import os
import random

 
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix='$', intents=intents)
 
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def gif(ctx):
    with open('allgif/gif1.gif', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        gifka = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=gifka)
bot.run('token')
