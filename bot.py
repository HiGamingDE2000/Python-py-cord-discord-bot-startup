import discord
import ezcord
from dotenv import load_dotenv

intents = discord.Intents.default()
activity = discord.Activity(type=discord.ActivityType.listening, name="online")
status = discord.Status.online # online, idle, dnd

bot = ezcord.Bot(
    intents=intents,
    activity=activity,
    status=status
)

load_dotenv()
bot.run(os.getenv("TOKEN"))
