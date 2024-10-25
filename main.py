import discord
from discord.ext import commands
import os
import keep_alive

# インテントを設定
intents = discord.Intents.default()
intents.messages = True  # メッセージ関連のインテントを有効化

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=intents)  # intentsを渡す

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Botの実行
if __name__ == "__main__":
    keep_alive.keep_alive()  # Flaskサーバーを起動
    bot.run(TOKEN)  # Botを実行
