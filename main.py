import discord
from logger import logging
from common.consts import *
from discord.ext import commands
from common.checkin_status import checkin

c = commands.Bot(command_prefix='~')
logger = logging.get_logger()


# 调用event
@c.event
async def on_ready():
    logger.info('Bot登入身份：' + str(c.user))
    game = discord.Game('牛子')
    await c.change_presence(activity=game)
    print("start success")

@c.command()
async def say(ctx, *args):
    await ctx.send(' '.join(args))


@c.command(name='安狗内')
async def angounei(ctx):
    await ctx.send('嗨害嗨')
    await ctx.send(':poop:')

checkin_task = checkin(bot=c, message='test message')
checkin_task.run()
c.run('')
