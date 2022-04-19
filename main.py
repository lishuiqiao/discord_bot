#導入 Discord.py
import discord
from logger import logging

#client 是我們與 Discord 連結的橋樑
client = discord.Client()

logger = logging.get_logger()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    logger.info('目前登入身份：' + str(client.user))

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')

client.run('ODU4MjEwMDIyMTA1NTQ2Nzcz.YNa0Xg.RhJUJDuHILbp5Wz8ae_BcNiL3yg') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面


