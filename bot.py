import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
activity = discord.Activity(type=discord.ActivityType.listening, name="online")
status = discord.Status.online # onlinr, idle, dnd

bot = discord.Bot(
    intents=intents,
    activity=activity,
    status=status
)

load_dotenv()
bot.run(os.getenv("TOKEN"))
