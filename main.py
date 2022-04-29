import discord
from logger import logging
from function import say
import instruction

client = discord.Client()

logger = logging.get_logger()

#调用event
@client.event
async def on_ready():
    logger.info('Bot登入身份：' + str(client.user))
    game = discord.Game('牛子')
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(instruction.Help.Say.value):
        await message.channel.send(say.Say(message.content))
    if message.content.startswith("安狗内"):
        await message.channel.send(say.Say(instruction.Help.Say.value + ' 嗨害嗨'))
        await message.channel.send(':poop:')

client.run('')


