import discord, asyncio, dotenv, os, logging, datetime, jishaku
from discord.ext import commands

bot = commands.AutoShardedBot(
    Intents=discord.Intents.all(), command_prefix=commands.when_mentioned_or("!")
)

if not os.path.isdir("logs"):
    os.mkdir("logs")
else:
    pass
now = datetime.datetime.now()
name = f"logs/{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}"
logger = logging.getLogger("Bot")
logger.setLevel(logging.INFO)
stream = logging.StreamHandler()
handler = logging.FileHandler(filename=f"{name}.log", encoding="utf-8", mode="w")
formatter = logging.Formatter("[%(asctime)s | %(name)s | %(levelname)s] %(message)s")
stream.setFormatter(formatter)
handler.setFormatter(formatter)
logger.addHandler(stream)
logger.addHandler(handler)

dotenv.load_dotenv(verbose=True)
token = os.getenv("BOT_TOKEN")

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

bot.run(token, bot=True, reconnect=True)
