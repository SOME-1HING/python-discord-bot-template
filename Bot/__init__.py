import os
import sys
import logging
import discord

from dotenv import load_dotenv
from discord.ext import commands

# Loading .env file
load_dotenv(os.path.join(".", ".env"))

# Clearing the log file
with open("bot_logs.txt", "w"):
    pass

# Set up Logging
FORMAT = "[Bot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("ptbcontrib.postgres_persistence.postgrespersistence").setLevel(
    logging.WARNING
)

LOGGER = logging.getLogger("[Bot]")
LOGGER.info(
    "Bot is starting. | Template by github.com/SOME-1HING (t.me/SOME1HING) | Licensed under MIT."
)

# Loading Token from .env file
try:
    TOKEN = os.environ["TOKEN"]
except KeyError:
    print("Please define the environment variable TOKEN")
    sys.exit(1)

"""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
"""
disIntents = discord.Intents.default()
disIntents.message_content = True
Client = commands.Bot(intents=disIntents, command_prefix="?", help_command=None)
