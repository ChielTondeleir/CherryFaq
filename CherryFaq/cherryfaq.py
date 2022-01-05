# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# Import the os module.
import os

#Import discord requirements
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Member

# Grab the API token from the .env file.
#DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = Bot('#')


bot.load_extension("cogs.cherryfaq")


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run("ENTER TOKEN HERE")