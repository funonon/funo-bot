import discord
from discord.ext import commands

# Botのトークン（環境変数などに保管するのがベスト）
TOKEN = 'your_token_here'  # GitHubに公開しないよう注意

# コマンドプレフィックスを指定
bot = commands.Bot(command_prefix='!')

# Bot起動時に通知するイベント
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# メッセージに応答するイベント
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Bot自身のメッセージは無視

    # 特定のメッセージに対する応答
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは！')

    # 他のコマンドも受け取る
    await bot.process_commands(message)

# 簡単なコマンドの追加例
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Botを実行
bot.run(TOKEN)
