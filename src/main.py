import discord
from discord.ext import commands
import os
import config
import jishaku
import colorlog
from config import LOGGER as logger

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix = "!",
            intents = discord.Intents.all(),
            owner_ids = [],
            # help_command = None
        )

        try:
            self.load_extension("jishaku")
            logger.info(f"✅ jishaku 로드 완료")
        except:
            logger.error(f"❎ jishaku 로드 실패")

        try:
            for filename in os.listdir("cogs"):
                if filename.endswith(".py"):
                    try:
                        self.load_extension(f"cogs.{filename[:-3]}")
                        logger.info(f"✅ {filename} 로드 완료")
                    except:
                        logger.error(f"❎ {filename} 로드 실패")
        except FileNotFoundError:
            for filename in os.listdir("src/cogs"):
                if filename.endswith(".py"):
                    try:
                        self.load_extension(f"cogs.{filename[:-3]}")
                        logger.info(f"✅ {filename} 로드 완료")
                    except:
                        logger.error(f"❎ {filename} 로드 실패")

    async def on_ready(self):
        logger.info(self.user)
        logger.info(self.user.id)
    
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

def setup_logger():
    logger.setLevel("DEBUG")
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "{log_color}{asctime} {message}", "[%y-%m-%d %H:%M:%S]", style="{"
        )
    )
    logger.addHandler(handler)
    logger.debug("Logging enabled")
    return logger


if __name__ == "__main__":
    setup_logger()
    bot = Bot()
    bot.run(config.BOT_TOKEN, reconnect=True)