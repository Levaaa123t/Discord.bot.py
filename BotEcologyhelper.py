from multiprocessing.spawn import get_command_line
import discord
from discord.ext import commands
import random
import os 


smiles1 = [':wave:', ':grinning:',':handshake:']
smiles2 = [':wave:', ':saluting_face:' ,':call_me:']
parting = ['Пока, надеюсь скоро увидимся ;)', 'Пока!', 'Пока! Главное не мусори!','До новых встреч!', 'Увидимся']
greetings = ['Привет! Я тебя ждал)', 'Приветик', 'Привет, как дела? Есть вопросы по очистке мусора?', 'Наконец то ты вернулся!:)', 'Привет! Я бот по экологии, я моуг помочь тебе!']
rubbish = {"Бутылка":"Выкидывай в контейнер с пластиком!",
           'Пачка чипсов':'Выкидывай в контейнер с пластиком!',
           'Стеклянная бутылка':'Выкидай в контейнер со стеклом!',
           'Стеклянная банка':'Выкидай в контейнер со стеклом!'
           }

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send("Пропиши команду #start чтобы начать! Или #helper чтобы посмотреть все команды")
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))
    await ctx.send(random.choice(smiles1))

@bot.command()
async def bye(ctx):
    await ctx.send(random.choice(parting))
    await ctx.send(random.choice(smiles2))

@bot.command()
async def start(ctx):
    await ctx.send('Привет! Я бот по экологии, я могу помочь тебе с выбрасыванием мусора, то есть скажу в какую мусорку, что нужно выкидывать! Чтобы я тебе помог напиши команду #throw (мусор)!')

@bot.command()
async def throw(ctx):
    if 'Бутылка' in rubbish:
        await ctx.send(rubbish['Бутылка'])
    elif 'Пачка чипсов' in rubbish:
        await ctx.send(rubbish['Пачка чипсов'])
    else:
        await ctx.send('У меня нет такого слова или ты ошибься!') 


run.bot('token')
