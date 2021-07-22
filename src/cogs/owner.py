from discord.ext import commands

import os
import itertools
import traceback
from humanize import naturalsize
from jishaku.modules import ExtensionConverter
from jishaku.paginators import WrappedPaginator


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command(
        name="load",
        aliases=["reload"],
        usage="[load|reload] [filename]",
        help="extensions를 로드/리로드 합니다.",
        # hidden=True,
    )
    @commands.is_owner()
    async def owner_reload(self, ctx, *extensions: ExtensionConverter):
        paginator = WrappedPaginator(prefix="", suffix="")

        for extension in itertools.chain(*extensions):
            method, icon = (
                (
                    self.bot.reload_extension,
                    "\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}",
                )
                if extension in self.bot.extensions
                else (self.bot.load_extension, "\N{INBOX TRAY}")
            )

            try:
                method(extension)
            except Exception as exc:  # pylint: disable=broad-except
                traceback_data = "".join(
                    traceback.format_exception(type(exc), exc, exc.__traceback__, 1)
                )

                paginator.add_line(
                    f"{icon}\N{WARNING SIGN} `{extension}`\n```py\n{traceback_data}\n```",
                    empty=True,
                )
            else:
                paginator.add_line(f"{icon} `{extension}`", empty=True)

        for page in paginator.pages:
            await ctx.send(page)

    @commands.command(
        name="unload",
        aliases=["언로드"],
        usage="unload [filename]",
        help="filename의 extension을 언로드합니다.",
        # hidden=True,
    )
    async def owner_unload(self, ctx, *extensions: ExtensionConverter):
        paginator = WrappedPaginator(prefix="", suffix="")
        icon = "\N{OUTBOX TRAY}"

        for extension in itertools.chain(*extensions):
            try:
                self.bot.unload_extension(extension)
            except Exception as exc:  # pylint: disable=broad-except
                traceback_data = "".join(
                    traceback.format_exception(type(exc), exc, exc.__traceback__, 1)
                )

                paginator.add_line(
                    f"{icon}\N{WARNING SIGN} `{extension}`\n```py\n{traceback_data}\n```",
                    empty=True,
                )
            else:
                paginator.add_line(f"{icon} `{extension}`", empty=True)

        for page in paginator.pages:
            await ctx.send(page)

    @commands.command(brief="Shutdown the Application")
    async def shutdown(self, ctx):
        await ctx.reply("OK! Shutdown the Application")
        await ctx.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))
