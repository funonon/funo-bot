import discord
from discord.ext import commands
import os

# 環境変数からトークンを取得
TOKEN = os.getenv('TOKEN')  # ReplitでTOKENをシークレットとして設定してください

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        
    async def setup_hook(self):
        # じゃんけんコマンドのCogをロード
        await self.load_extension("じゃんけん")
    
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.tree.sync()  # スラッシュコマンドの同期

# インテント設定
intents = discord.Intents.default()
intents.message_content = True

# Botのインスタンスを作成
bot = MyBot(command_prefix="!", intents=intents)

# Botの実行
bot.run(TOKEN)

