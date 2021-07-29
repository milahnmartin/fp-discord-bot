import time
import discord
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle
import fpdata
import requests

def main():
    bot = commands.Bot(command_prefix=".")

    status = cycle(
        [
            "https://fingerprintza.com/",
            "Visit our Twitter @fingerprintza",
            "Register Today, fingerprintza.com/register-section",
            ".commands",
        ]
    )
    emojiFinger = "<:Fingerprint:813383545065439253>"
    emojiOne = "<>"
    @tasks.loop(seconds=15)
    async def change_status():
        await bot.change_presence(activity=discord.Game(next(status)))

    @bot.event
    async def on_ready():
        change_status.start()
        print("The Bot Fingerprint ZA Has Started...")

    @bot.command()
    async def faceit(ctx,player='Ultrafy',map=None):
        try:
            fpdata.create_log_sql('unknown','!faceit',player)

            response = requests.get(f"http://127.0.0.1:5000/get/{player}/faceit:{map}")
            data = response.json()
            if not map:
                data = data['lifetime']
                wins_status = []
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
                await ctx.send("Busy fetching fpdata!", delete_after=3.0)
                embed = discord.Embed(
                    title="Player Information",
                    description="All Available fpdata about the player is stated below.",
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
            else:
                data = data['segments']
                map_name = data['label']
                data = data[0]
                map_stats = data['stats']
                AverageAssists = maps_stats['Average Assists']
                AverageDeaths = maps_stats['Average Deaths']
                AverageHeadshots = maps_stats['Average Headshots %']
                AverageKDRatio = maps_stats['Average K/D Ratio']
                AverageKills = maps_stats['Average Kills']
                AverageMVP = maps_stats['Average MVPs']
                AveragePentaKills = maps_stats['Average Penta Kills']
                AverageQuadroKills = maps_stats['Average Quadro Kills']
                AverageTripleKills = maps_stats['Average Triple Kills']
                DeathsTotal = maps_stats['Deaths']
                HeadshotsTotal = maps_stats['Headshots']
                KillsTotal = maps_stats['Kills']
                TotalMatches = maps_stats['Matches']
                MVPsTotal = maps_stats['MVPs']
                RoundsTotal = maps_stats['Rounds']
                WinsTotal = maps_stats['Wins']



                embed = discord.Embed(
                    title="Player Map information",
                    description="All Available fpdata about the player's map is stated below.",
                    colour=discord.Colour.teal(),
                )

                embed.set_footer(
                    text="Twitter: @fingerprintza "
                )
                embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
                embed.add_field(name="**__Player:__**", value=player, inline=False)
                embed.add_field(name="**__Map:__**", value=map_name, inline=False)
                embed.add_field(name="**__Average Assists:__**", value=AverageAssists, inline=False)
                embed.add_field(name="**__Average Deaths:__**", value=AverageDeaths, inline=False)
                embed.add_field(name="**__Average Headshot %:__**", value=AverageHeadshots, inline=False)
                embed.add_field(name="**__Average K/D Ratio:__**", value=AverageKDRatio, inline=False)
                embed.add_field(name="**__Average Kills:__**", value=AverageKills, inline=False)
                embed.add_field(name="**__Average MVP's:__**", value=AverageAssists, inline=False)
                embed.add_field(name="**__Average Penta Kills:__**", value=AveragePentaKills, inline=False)
                embed.add_field(name="**__Average Quadro Kills:__**", value=AverageQuadroKills, inline=False)
                embed.add_field(name="**__Average Triple Kills:__**", value=AverageTripleKills, inline=False)
                embed.add_field(name="**__Total Dethas:__**", value=DeathsTotal, inline=False)
                embed.add_field(name="**__Total Headshots:__**", value=HeadshotsTotal, inline=False)
                embed.add_field(name="**__Total Kills:__**", value=KillsTotal, inline=False)
                embed.add_field(name="**__Total MVP's:__**", value=MVPsTotal, inline=False)
                embed.add_field(name="**__Total Rounds Played:__**", value=RoundsTotal, inline=False)
                embed.add_field(name="**__Total Wins:__**", value=WinsTotal, inline=False)

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



    @bot.command(aliases=["commands"])
    async def fingerprintcommands(ctx):
        await ctx.send("Getting Commands!", delete_after=3.0)
        embed = discord.Embed(
            title="Commands",
            description="All Available Commands.",
            colour=discord.Colour.teal(),
        )

        embed.set_footer(
            text="Website: https://fingerprintza.com/ | Twitter: @fingerprintza "
        )
        embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
        embed.add_field(
            name="**__.faceit:__** {player name}",
            value="Shows Faceit Stats of player",
            inline=False,
        )
        await ctx.send(embed=embed)

    bot.run("ODA1NDYxMzY4MDU1NTI5NTAy.YBbOWg.5R4C0JzxrIaNl3jmZYpNR6E8_lc")


if __name__ == '__main__':
    main()