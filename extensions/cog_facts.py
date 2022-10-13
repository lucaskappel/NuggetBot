import json, random
import discord
from discord.ext import commands
from discord import app_commands


class Cog_Facts(commands.Cog):

    def __init__(self, bot_client: commands.Bot) -> None:
        self.bot_client = bot_client
        self.nugget_facts = {"Nugget facts didn't load :( Go yell at Bard#3883!! >:[]"}
        self.last_nugget_fact = ""
        with open(r"resources/nugget_facts.json", encoding='utf8') as config_file:  # open the existing config
            self.nugget_facts = json.load(config_file)  # Load the config's contents
        
#### #### #### ####

    @app_commands.command(name="nugget_facts")
    async def sc_nugget_fact(self, interaction: discord.Interaction):
        next_nugget_fact = self.nugget_facts[random.choice([fact_name for fact_name in self.nugget_facts])]
        while next_nugget_fact == self.last_nugget_fact: # Don't give the same fact twice in a row!
            next_nugget_fact = self.nugget_facts[random.choice([fact_name for fact_name in self.nugget_facts])]
        await interaction.response.send_message(next_nugget_fact)

        
#### #### #### ####


async def setup(bot_client: commands.Bot) -> None:
    await bot_client.add_cog(Cog_Facts(bot_client))
