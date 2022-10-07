import discord
from discord.ext import commands
from discord import app_commands


class Cog_Template(commands.Cog):

    def __init__(self, bot_client: commands.Bot) -> None:
        self.bot_client = bot_client
        
#### #### #### ####
    
    async def slash_command_coroutine( # Must return 25 or fewer choices
            self, interaction: discord.Interaction, current_user_input: str,) -> list[app_commands.Choice]:
        autocomplete_list = [f"option{n}:{interaction.id}" for n in range(0, 24)]
        return [
            app_commands.Choice(name=autocomplete_option, value=autocomplete_option)
            for autocomplete_option in autocomplete_list if current_user_input.lower() in autocomplete_option.lower()
        ]

    @app_commands.command(name="slash_command_template")
    @app_commands.autocomplete(query=slash_command_coroutine)
    async def slash_resource(self, interaction: discord.Interaction, query: str):
        await interaction.response.send_message(query)
        
#### #### #### ####


async def setup(bot_client: commands.Bot) -> None:
    await bot_client.add_cog(Cog_Template(bot_client))
