import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option
from discord.commands import message_command, user_command
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
activity = discord.Activity(type=discord.ActivityType.listening, name="ticket")
status = discord.Status.idle

bot = discord.Bot(
    intents=intents,
    activity=activity,
    status=status
)

if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")


@discord.guild_only()
@discord.default_permissions(administrator=True)
@commands.has_permissions(administrator=True)
@bot.slash_command(description="Lass den Bot eine Nachricht senden")
async def say(
        ctx,
        text: Option(str, "Der Text, den du senden möchtest"),
        channel: Option(discord.TextChannel, "Der Channel, in den du die Nachricht senden möchtest")
):
    await channel.send(text)
    await ctx.respond("Nachricht gesendet", ephemeral=True)

load_dotenv()
bot.run(os.getenv("TOKEN"))