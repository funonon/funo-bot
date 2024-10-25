import discord
from discord import app_commands
from discord.ext import commands
import random

class Janken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /じゃんけん コマンドの定義
    @app_commands.command(name="じゃんけん", description="Botとじゃんけんをします")
    @app_commands.describe(choice="出す手を選んでください")
    @app_commands.choices(
        choice=[
            discord.app_commands.Choice(name="グー", value="グー"),
            discord.app_commands.Choice(name="チョキ", value="チョキ"),
            discord.app_commands.Choice(name="パー", value="パー"),
        ]
    )
    async def janken(self, interaction: discord.Interaction, choice: discord.app_commands.Choice[str]):
        user_choice = choice.value  # ユーザーの選択を取得
        options = ["グー", "チョキ", "パー"]
        
        # Botの手をランダムに選ぶ
        bot_choice = random.choice(options)
        
        # ユーザーの選択とBotの選択を比較
        if user_choice == bot_choice:
            result = "引き分けです！"
        elif (user_choice == "グー" and bot_choice == "チョキ") or \
             (user_choice == "チョキ" and bot_choice == "パー") or \
             (user_choice == "パー" and bot_choice == "グー"):
            result = "あなたの勝ちです！"
        else:
            result = "あなたの負けです！"

        # 結果を送信
        await interaction.response.send_message(
            f"あなた: {user_choice}\nBot: {bot_choice}\n結果: {result}"
        )

# Botにコグを追加するための関数
async def setup(bot):
    await bot.add_cog(Janken(bot))
