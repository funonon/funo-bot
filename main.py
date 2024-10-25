import discord
from discord.ext import commands
import os

# 環境変数からトークンを取得
TOKEN = os.getenv('TOKEN')  # ReplitなどでTOKENをシークレットとして設定してください

# Bot用のカスタムクラス
class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        # 親クラスの__init__を呼び出し、プレフィックスとインテントを設定
        super().__init__(command_prefix=command_prefix, intents=intents)
        
        # Botの初期化時にメッセージを表示
        print("Bot is being initialized!")

    # Bot起動時に通知するイベント
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    # メッセージを受け取ったときのイベント
    async def on_message(self, message):
        if message.author == self.user:
            return  # Bot自身のメッセージは無視

        # 特定のメッセージに対する応答
        if message.content == 'こんにちは':
            await message.channel.send('こんにちは！')

        # 他のコマンドも受け取る
        await self.process_commands(message)

# Botのインテント設定（必要な権限に応じて調整）
intents = discord.Intents.default()
intents.message_content = True  # メッセージの内容を取得する権限が必要な場合

# Botのインスタンスを作成
bot = MyBot(command_prefix='!', intents=intents)

# コマンドの追加例
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Botの実行
bot.run(TOKEN)
