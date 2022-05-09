import asyncio
import datetime
import time
import discord
from utils.auto_checkin_sender import *

from common.consts import *
from discord.ext import tasks, commands

class checkin(commands.Cog):
    def __init__(self, bot, message=None):
        self.first_run_flag = True
        self.bot = bot
        self.message = message

    def run(self):
        self.messageDaily.start()

    # loop for sending message
    @tasks.loop(hours=24)
    async def messageDaily(self):
        if self.first_run_flag:
            await asyncio.sleep(self.offset())
            print("busy_wait over")
            self.first_run_flag = False
        logs = formatted_logs()
        for k, v in logs:
            if k == "luansiqi":
                await self.DirectMessageCheckinLog(v, ids.luansiqi.value)
            if k == "chenannan":
                await self.DirectMessageCheckinLog(v, ids.chenannan.value)


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

    async def DirectMessageCheckinLog(self, messge, id):
        user = await self.bot.fetch_user(id)
        embed = discord.Embed(
            title="{}: below is {}'s mihoyo bbs checkin log today".
                format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), user.name),
            color=0xF1C40F
        )
        embed.description = messge

        await user.create_dm()  # 创建私信通道
        await user.dm_channel.send(embed=embed)  # 向用户发送私信

