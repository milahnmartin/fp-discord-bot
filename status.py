import time
import discord
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix=".")
status = cycle(
    [
        "https://fingerprintza.com/",
        "Visit our Twitter @fingerprintza",
        "Register Today, fingerprintza.com/register-section",
        ".commands",
    ]
)

emojiF = "<:Fingerprint:813383545065439253>"

# Set Message when Bot is online
@bot.event
async def on_ready():
    change_status.start()
    print("The Bot Fingerprint ZA Has Started...")


# Set Bot status
@tasks.loop(seconds=15)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))