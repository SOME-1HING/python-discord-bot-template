from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping Command: ?ping
    @commands.command()
    async def ping(self, ctx: commands.Context):
        ping_time = self.bot.latency * 1000
        await ctx.reply(
            f"Pong! : {round(ping_time)}ms \nApparently, I'm quicker than our server members"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
