import time
import discord
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle
from status import * 
import os

# Set Prefix
bot = commands.Bot(command_prefix=".")

# bot.load_extension(R"C:\Users\henri\OneDrive\Documents\Fingerprint V2\fp-discord-bot\testing")
for filename in os.listdir('./fp-discord-bot'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("ODA1NDYxMzY4MDU1NTI5NTAy.YBbOWg.XsiSr2q6TMm19m_4UJZHJvhfgxE")
