from multiprocessing.spawn import get_command_line
import discord
from discord.ext import commands
import random
from botmem import mem
import os 

smiles1 = [':wave:', ':grinning:',':handshake:']
smiles2 = [':wave:', ':saluting_face:' ,':call_me:']
parting = ['Пока, надеюсь скоро увидимся ;)', 'Пока!', 'До новых встреч!', 'Увидимся']
greetings = ['Привет! Я тебя ждал)', 'Приветик', 'Привет, как дела?', 'Наконец то ты вернулся!:)', 'Привет! Я бот my server #5606!']
gifki = ['https://images-ext-1.discordapp.net/external/J0eC-lZGcxJyq1AVf7lpHSZT7VeEEV2sKHdN1hNunHU/https/media.tenor.com/epNMHGvRyHcAAAPo/gigachad-chad.mp4',
         'https://images-ext-1.discordapp.net/external/jSTmkcQYpEccmcr7a_3JfSDr5HuGFxXNLwLhlzEIby8/%3Fv%3D1/https/cdn.discordapp.com/emojis/852259524600922173.gif?width=140&height=140',
         'https://images-ext-1.discordapp.net/external/-3u8gs5oXxG6HEUd7iuXObqf1TpVa1uTRTfj0zMFVoA/https/media.tenor.com/XvoY2p2VdyAAAAPo/emoji-summer.mp4',
         'https://images-ext-1.discordapp.net/external/hGD4RIUiQQ2RJ-j8vWTWrCvP3VHyQwzjwNDScaQe_FI/https/media.tenor.com/OOslTDt3rHAAAAPo/penguin-of-madagascar.mp4',
         'https://images-ext-2.discordapp.net/external/ltfIAjiUD1G8UBMtGqa4dmwi-zSjGEZY8KQA6gUL1MI/https/media.tenor.com/9RCIDZjkhBsAAAPo/hamster-meme.mp4',
         'https://images-ext-1.discordapp.net/external/lR9qvPvWI0m4EOeoTi9tmB6x91nFQKosP-ElStH8ybY/https/media.tenor.com/JZxEu1mBeGwAAAPo/esqueleto.mp4',
         'https://images-ext-2.discordapp.net/external/WpAG9WB8rorwWtlwNu3EwPv0y7Tnp0P4fK1_FCCW6Do/https/media.tenor.com/aQmJti4EuhoAAAPo/%25D1%2581%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B6%25D0%25BE%25D1%2584%25D0%25B0%25D0%25B3%25D0%25B8-%25D0%25B4%25D0%25B6%25D0%25BE%25D0%25B4%25D0%25B6%25D0%25BE%25D1%2584%25D0%25B0%25D0%25B3%25D0%25B8.mp4']

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
async def helper(ctx):
    await ctx.send(all_comands)

@bot.command()
async def gif(ctx):
    await ctx.send(random.choice(gifki))





bot.run("Token")





