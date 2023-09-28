import discord
import random
from bot_logic import gen_pass

smiles1 = [':wave:', ':grinning:',':handshake:']
smiles2 = [':wave:', ':saluting_face:' ,':call_me:']
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("$gen_pass"):
        character_num = int(message.content.split() [1])
        print(character_num)
        generated_password = gen_pass(character_num)
        await message.channel.send(generated_password)
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
        await message.channel.send (random.choice(smiles1))
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye bye")
        await message.channel.send(random.choice(smiles2))
    else:
        await message.channel.send(message.content)


client.run('MTE1MjYwMDY2NzYwNTcwODg2MA.GCGhIi.lNt5YYMhssmK9VcM5vx_SBMVokp0ENgqyDKHMc')
