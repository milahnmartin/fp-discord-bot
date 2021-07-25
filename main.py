import time
import discord
from discord import Color
from discord.ext import commands, tasks
import requests
from requests import api
from requests.api import head
from api import *

# Set Prefix
bot = commands.Bot(command_prefix=".")


@bot.command()
async def faceit(ctx,player='Ultrafy'):
    try:
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
        embed.add_field(name="**__Recent Games:__**", value=recent, inline=False)
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