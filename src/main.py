from discord.ext import commands
import os
import config
import jishaku
import colorlog
from config import LOGGER as logger

bot = commands.AutoShardedBot(
    Intents=__import__("discord").Intents.all(), command_prefix=commands.when_mentioned_or("!")
)

if not os.path.isdir("logs"):
    os.mkdir("logs")
else:
    pass

try:
    bot.load_extension("jishaku")
    logger.info(f"✅ jishaku 로드 완료")
except:
    logger.error(f"❎ jishaku 로드 실패")

try:
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{filename[:-3]}")
                logger.info(f"✅ {filename} 로드 완료")
            except:
                logger.error(f"❎ {filename} 로드 실패")
except FileNotFoundError:
    for filename in os.listdir("src/cogs"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{filename[:-3]}")
                logger.info(f"✅ {filename} 로드 완료")
            except:
                logger.error(f"❎ {filename} 로드 실패")

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
    bot = bot()
    bot.run(config.BOT_TOKEN, reconnect=True)