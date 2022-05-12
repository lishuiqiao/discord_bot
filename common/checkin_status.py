import asyncio
import datetime
import time
from logger import logging

import discord
from utils.auto_checkin_sender import *

from common.consts import *
from discord.ext import tasks, commands

logging = logging.get_logger()

class checkin(commands.Cog):
    def __init__(self, bot, message=None):
        self.bot = bot
        self.message = message

    def run(self):
        self.messageDaily.start()

    # loop for sending message
    @tasks.loop(hours=24)
    async def messageDaily(self):
        logs = formatted_logs()
        if logs:
            if "luansiqi" in logs:
                await self.DirectMessageCheckinLog(logs["luansiqi"], ids.luansiqi.value)
            if "chenannan" in logs:
                await self.DirectMessageCheckinLog(logs["chenannan"], ids.chenannan.value)

            if "summary" in logs:
                await self.DirectMessage(logs["summary"], "summary of logs", ids.luansiqi.value)
        else:
            await self.DirectMessageCheckinLog('no log', ids.luansiqi.value)

    @messageDaily.before_loop
    async def before(self):
        # 首次运行直接调取一次log
        logs = formatted_logs()
        await self.bot.wait_until_ready()
        if logs:
            if "luansiqi" in logs:
                print(logs)
                await self.DirectMessageCheckinLog(logs["luansiqi"], ids.luansiqi.value)
            if "chenannan" in logs:
                await self.DirectMessageCheckinLog(logs["chenannan"], ids.chenannan.value)

            if "summary" in logs:
                await self.DirectMessage(logs["summary"], "summary of logs", ids.luansiqi.value)
        else:
            await self.DirectMessageCheckinLog('no log', ids.luansiqi.value)
        # 等待至下一次运行时间
        await asyncio.sleep(self.offset())

    # %H:%M:%S
    def offset(self):
        # 获取现在时间
        now_time = datetime.datetime.now()
        # 获取第一次运行时间
        if now_time.time().hour < 12:
            time_diff = (datetime.datetime(year=now_time.date().year, month=now_time.date().month,
                                           day=now_time.date().day,
                                           hour=12, minute=0, second=0) - now_time).total_seconds()
            return time_diff
        else:
            time_diff = (datetime.datetime(year=now_time.date().year, month=now_time.date().month,
                                           day=now_time.date().day + 1,
                                           hour=12, minute=0, second=0) - now_time).total_seconds()
            return time_diff

    async def DirectMessageCheckinLog(self, message, id):
        user = await self.bot.fetch_user(id)
        embed = discord.Embed(
            title="{}: below is {}'s mihoyo bbs checkin log today".
                format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), user.name),
            color=0xF1C40F
        )
        embed.description = message

        try:
            await user.create_dm()  # 创建私信通道
            await user.dm_channel.send(embed=embed)  # 向用户发送私信
        except Exception as e:
            logging.error(e, exc_info=True)

    async def DirectMessage(self, message, title, id):
        user = await self.bot.fetch_user(id)
        embed = discord.Embed(
            title=title,
            color=0xF1C40F
        )
        embed.description = message

        try:
            await user.create_dm()  # 创建私信通道
            await user.dm_channel.send(embed=embed)  # 向用户发送私信
        except Exception as e:
            logging.error(e, exc_info=True)

