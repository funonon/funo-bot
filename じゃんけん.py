import discord
from discord.ext import commands
from discord import app_commands
import random

class Janken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="じゃんけん", description="じゃんけんをします")
    async def janken(self, interaction: discord.Interaction):
        choices = ["グー", "チョキ", "パー"]
        bot_choice = random.choice(choices)

        await interaction.response.send_message(f"あなたの手: 選択してください", view=JankenView(bot_choice))

class JankenView(discord.ui.View):
    def __init__(self, bot_choice):
        super().__init__()
        self.bot_choice = bot_choice

    @discord.ui.button(label="グー", style=discord.ButtonStyle.primary)
    async def rock(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.check_winner(interaction, "グー")

    @discord.ui.button(label="チョキ", style=discord.ButtonStyle.primary)
    async def scissors(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.check_winner(interaction, "チョキ")

    @discord.ui.button(label="パー", style=discord.ButtonStyle.primary)
    async def paper(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.check_winner(interaction, "パー")

    async def check_winner(self, interaction, user_choice):
        bot_choice = self.bot_choice
        if user_choice == bot_choice:
            result = "引き分け！"
        elif (user_choice == "グー" and bot_choice == "チョキ") or \
             (user_choice == "チョキ" and bot_choice == "パー") or \
             (user_choice == "パー" and bot_choice == "グー"):
            result = "あなたの勝ち！"
        else:
            result = "あなたの負け！"
        await interaction.response.edit_message(content=f"あなたの手: {user_choice}\nボットの手: {bot_choice}\n{result}", view=None)

async def setup(bot):
    await bot.add_cog(Janken(bot))  # awaitで非同期に
