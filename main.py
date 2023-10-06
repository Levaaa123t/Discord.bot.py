from multiprocessing.spawn import get_command_line
import discord
from discord.ext import commands
import random
import os 
import requests 

smiles1 = [':wave:', ':grinning:',':handshake:']
smiles2 = [':wave:', ':saluting_face:' ,':call_me:']
parting = ['Пока, надеюсь скоро увидимся ;)', 'Пока!', 'До новых встреч!', 'Увидимся']
greetings = ['Привет! Я тебя ждал)', 'Приветик', 'Привет, как дела?', 'Наконец то ты вернулся!:)', 'Привет! Я бот my server #5606!']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

all_comands = ['$hello - приветствие', '$bye - прощание', '$heh (число) - отправляет смех хех', 'gen_pass (число) - генерирует пароль который ты хочешь', '$add(число + число) - скалдывает написанные числа', 
           '$multiplication(число * число) - умножает написанные числа', '$subtraction(число - число) - вычитает написанные числа', '$division(число ÷ число) - делит написанные числа',
           '$mem - присылает мем', '$gif - присылает гифку', '$duck - присылает картинку или гифку с уткой', '$dog - присылает картинку или гифку с собакой']


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))
    await ctx.send(random.choice(smiles1))

@bot.command()
async def bye(ctx):
    await ctx.send(random.choice(parting))
    await ctx.send(random.choice(smiles2))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def gen_pass(ctx,pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    pass_length = int(pass_length)
    for i in range(pass_length):
        password += random.choice(elements)

    await ctx.send(password)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def  multiplication(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def  subtraction(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def  division(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def helper(ctx):
    await ctx.send(all_comands)

@bot.command()
async def gif(ctx):
    gif_list = os.listdir('allgif')
    random_gif = random.choice(gif_list)
    with open(f'allgif/{random_gif}', 'rb') as f:
        gifka = discord.File(f)
    await ctx.send(file=gifka)

@bot.command()
async def mem(ctx):
    mems_list = os.listdir('images')
    random_mem = random.choice(mems_list)
    with open(f'images/{random_mem}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url ='https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''По команде cat вызывает функцию get_cat_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)




bot.run("Token")





