import aiohttp
import json
import discord
from discord.ext import commands
from discord import app_commands


class Cog_NASA(commands.Cog):

    def __init__(self, bot_client: commands.Bot) -> None:
        self.bot_client = bot_client
        self.bot_config = {} # reload the config because im lazy and think like a monkey
        with open(r"config.json", encoding='utf8') as config_file:  # open the existing config
            self.bot_config = json.load(config_file)  # Load the config's contents

#### #### #### ####

    @app_commands.command(name="nasa_apod")
    async def sc_nasa_apod(self, interaction: discord.Interaction):

        # First defer the response, no clue how long the api will take.
        await interaction.response.defer(thinking=False)

        # Build the GET url.
        api_url = r"https://api.nasa.gov/planetary/apod" + f"?api_key={self.bot_config['nasa_api_token']}"

        # Get the data from nasa's api
        json_response = {}
        async with aiohttp.ClientSession() as client_session:
            async with client_session.get(url=api_url) as request_response:
                json_response = await request_response.json()

        # Build and send the response.
        embed_apod = discord.Embed(
            title=f"Astronomy Picture of the Day\n{json_response['title']}",
            url=json_response['hdurl'],
            description=json_response['explanation']
        )
        if 'copyright' in json_response.keys(): embed_apod.title = embed_apod.title + f"\n{json_response['copyright']}"

        embed_apod.set_image(url=json_response['hdurl'])
        await interaction.followup.send(embed=embed_apod)

#### #### #### ####


async def setup(bot_client: commands.Bot) -> None:
    await bot_client.add_cog(Cog_NASA(bot_client))
