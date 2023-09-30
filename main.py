from multiprocessing.spawn import get_command_line
import discord
from discord.ext import commands
import random

smiles1 = [':wave:', ':grinning:',':handshake:']
smiles2 = [':wave:', ':saluting_face:' ,':call_me:']
parting = ['Пока, надеюсь скоро увидимся ;)', 'Пока!', 'До новых встреч!', 'Увидимся']
greetings = ['Привет! Я тебя ждал)', 'Приветик', 'Привет, как дела?', 'Наконец то ты вернулся!:)', 'Привет! Я бот my server #5606!']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

all_comands = ['$hello - приветствие', '$bye - прощание', '$heh (число) - отправляет смех хех', 'gen_pass (число) - генерирует пароль который ты хочешь', '$add(число + число) - скалдывает написанные числа', 
           '$multiplication(число * число) - умножает написанные числа', '$subtraction(число - число) - вычитает написанные числа', '$division(число ÷ число) - делит написанные числа']

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
async def help(ctx):
    await ctx.send(all_comands)






bot.run("ТОКЕН")
