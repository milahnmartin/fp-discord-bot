import time
import discord
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle
from api import *

bot = commands.Bot(command_prefix=".")

status = cycle(
    [
        "https://fingerprintza.com/",
        "Visit our Twitter @fingerprintza",
        "Register Today, fingerprintza.com/register-section",
        ".commands",
    ]
)
@tasks.loop(seconds=15)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
    
@bot.event
async def on_ready():
    change_status.start()
    print("The Bot Fingerprint ZA Has Started...")

@bot.command()
async def faceit(ctx,player='Ultrafy'):

    try:
        wins_status = []
        my_player = Faceit(player)
        data = my_player.get_player_stats()
        wins = data["Wins"]
        matches = data["Matches"]
        winr = data["Win Rate %"]
        recent = data["Recent Results"]
        longest = data["Longest Win Streak"]
        current = data["Current Win Streak"]
        headshot = data["Total Headshots %"]
        avgheadshot = data["Average Headshots %"]
        kd = data["Average K/D Ratio"]

        for i in recent:
            if i == '1':
                wins_status.append('W')
            else:
                wins_status.append('L')


        await ctx.send("Busy fetching data!", delete_after=3.0)
        embed = discord.Embed(
            title="Player Information",
            description="All Available data about the player is stated below.",
            colour=discord.Colour.teal(),
        )

        embed.set_footer(
            text="Twitter: @fingerprintza "
        )
        embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
        embed.add_field(name="**__Player:__**", value=player, inline=False)
        embed.add_field(name="**__Wins:__**", value=wins, inline=False)
        embed.add_field(name="**__Matches:__**", value=matches, inline=False)
        embed.add_field(name="**__Win Rate:__**", value=winr, inline=False)
        embed.add_field(name="**__Recent Games:__**", value=wins_status, inline=False)
        embed.add_field(name="**__Longest Win Streak:__**", value=longest, inline=False)
        embed.add_field(name="**__Current Win Streak:__**", value=current, inline=False)
        embed.add_field(name="**__Total Headshots:__**", value=headshot, inline=False)
        embed.add_field(name="**__Average Headshot %:__**", value=avgheadshot, inline=False)
        embed.add_field(name="**__K/D Ratio:__**", value=kd, inline=False)

        await ctx.send(embed=embed)
    except KeyError:
        embed = discord.Embed(
            title=player,
            description="is not registered on Faceit.",
            colour=discord.Colour.teal(),
        )

        embed.set_footer(
            text="Twitter: @fingerprintza "
        )
        embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
        await ctx.send(embed=embed)



bot.run("ODA1NDYxMzY4MDU1NTI5NTAy.YBbOWg.5R4C0JzxrIaNl3jmZYpNR6E8_lc")