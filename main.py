import discord
from discord.ext import commands
import os
import keep_alive  # Replitのためのファイルをインポート

TOKEN = os.getenv('TOKEN')  # ReplitでTOKENをシークレットとして設定

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self):
        # コグをロードする場合はここで行う
        pass

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.tree.sync()  # スラッシュコマンドの同期

# インテント設定
intents = discord.Intents.default()
intents.message_content = True

# Botのインスタンスを作成
bot = MyBot(command_prefix="!", intents=intents)

# Botの実行
if __name__ == "__main__":
    keep_alive.keep_alive()  # サーバーを立てる
    bot.run(TOKEN)
