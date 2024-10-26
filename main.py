import discord
from discord.ext import commands
import os
import keep_alive
import asyncio

# インテントを設定
intents = discord.Intents.default()
intents.messages = True  # メッセージ関連のインテントを有効化

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  # スラッシュコマンドを同期
    print(f'Logged in as {bot.user}')

async def load_extensions():
    await bot.load_extension('じゃんけん')  # じゃんけんコマンドのエクステンションをロード

# Botの実行
if __name__ == "__main__":
    keep_alive.keep_alive()  # Flaskサーバーを起動

    # イベントループ内でbotとエクステンションを非同期起動
    asyncio.run(load_extensions())
    bot.run(TOKEN)
