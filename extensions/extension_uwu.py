import aiohttp
import discord
from discord.ext import commands
from discord import app_commands


@app_commands.context_menu(name="UWU-ify! >.<")
async def cm_uwuify(interaction: discord.Interaction, message: discord.Message):
    if message.author.id == 183033825108951041:
        await interaction.response.send_message(message.content)
        return
    await interaction.response.defer(thinking=False)
    await interaction.followup.send(await uwu_text_async(message.content))


async def uwu_text_async(text_to_uwu):
    async with aiohttp.ClientSession() as client_session:
        async with client_session.post(
                url=r"https://uwuaas.herokuapp.com/api/", json={"text": text_to_uwu}) as request_response:

            if request_response.status != 200:
                print(f"UWU post failed: <{request_response.status}>")
            return (await request_response.json())["text"]


async def setup(bot_client: commands.Bot) -> None:
    bot_client.tree.add_command(cm_uwuify)
