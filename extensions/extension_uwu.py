import requests
import discord
from discord.ext import commands
from discord import app_commands


@app_commands.context_menu(name="UWU-ify! >.<")
async def cm_uwuify(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(uwu_text(message.content))


def uwu_text(text_to_uwu):
    request_response = requests.post(url=r"https://uwuaas.herokuapp.com/api/", json={"text": text_to_uwu})
    if request_response.status_code != 200:
        print(f"UWU post failed: <{request_response.status_code}>")
    return request_response.json()["text"]


async def setup(bot_client: commands.Bot) -> None:
    bot_client.tree.add_command(cm_uwuify)
