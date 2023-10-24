import sys
from Bot import LOGGER, Client, TOKEN, cogs


# When bot is ready (Bot start)
@Client.event
async def on_ready():
    # Loading Cogs
    await cogs.alive.setup(Client)
    await cogs.ping.setup(Client)

    LOGGER.info(f"Bot is Ready and Online as {Client.user.name}")


if __name__ == "__main__":
    try:
        Client.run(TOKEN)
    except KeyboardInterrupt:
        LOGGER.info("Bot stopped by the user")
        sys.exit(0)
