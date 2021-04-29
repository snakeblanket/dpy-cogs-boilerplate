import os
from discord.ext import commands


class Owner_Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command(brief="Load Extension")
    async def reload(self, ctx, path):
        self.bot.load_extension(f"cogs.{path}")
        await ctx.reply("Successfully reloaded cogs.{}".format(path))

    @commands.command(brief="Shutdown the Application")
    async def shutdown(self, ctx):
        await ctx.reply("OK! Shutdown the Application")
        await ctx.bot.logout()


def setup(bot):
    bot.add_cog(Owner_Example(bot))
