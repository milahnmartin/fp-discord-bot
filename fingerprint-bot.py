import discord 
import requests
import json
import pyrebase
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle


#Set Prefix
bot = commands.Bot(command_prefix = '!') 
status = cycle(['https://fingerprintza.com/', 'Bot created by MrT1TAN#3244'])

#Set Message when Bot is online
@bot.event 
async def on_ready():
  change_status.start()
  print('Hello, I\'m online')

#On error Command
@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.send('You don\'t have the Permision to use this command 😕', delete_after = 5)
    await ctx.message.delete()
  elif isinstance(error,commands.MissingRequiredArgument):
    await ctx.send('Please enter all the required arguements ⌨️', delete_after = 5)
    await ctx.message.delete()
  else:
    raise error

#Auto Role Command
@bot.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 805537263617703996:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

    if payload.emoji.name == 'Agree':
      role = discord.utils.get(guild.roles, name='Members')

    if role is not None:
      member = payload.member
      if member is not None:
        await member.add_roles(role)
        print('Done')
      else:
        print('Member not found.')

#Purge command
@bot.command(aliases =['p'])
async def purge(ctx, amount = 5):
 await ctx.channel.purge(limit=amount)
 await ctx.send(str(amount) + ' messages deleted!!', delete_after = 5)


#Testing Command
@bot.command()
async def Testing(ctx):
 msg = await ctx.send(':Statusgreen:')
 await msg.add_reaction('<:Statusgreen:805475295573442560>')

#Testing2
@bot.command() 
async def Testing2(ctx):
  await ctx.send('Busy fetching data!', delete_after=3.0)
  
  embed = discord.Embed(
    title = 'Your Title', 
    description =  'Your Description [Twitter](https://twitter.com/MrT1TAN)',
    colour = discord.Colour.blue()
  )
  await ctx.send(embed=embed)


#Embeds
@bot.command() 
async def ebmsg(ctx, ebtitle='Default'):
  embed = discord.Embed(
    title = ebtitle, 
    description =  '',
    colour = discord.Colour.red()
  )
  embed.set_author(name= '')
  embed.set_footer(text='Made by MrT1TAN#3244')
  #embed.set_thumbnail(url='.png')
  embed.add_field(name='Tesxt', value='asd', inline=False)
  await ctx.send(embed=embed)


#StatusgreenCommand
@bot.command() 
@commands.has_permissions(manage_messages = True)
async def Statusgreen(ctx):
  channel = bot.get_channel(805159215370076191)
  embed = discord.Embed(
    title = 'ZA FingerPrint Status', 
    description =  '',
    colour = discord.Colour.green()
  )
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name='**Status:**', value='\n **All ZA FingerPrint Services are currently running** 🟢 ', inline=True)
  await channel.send(embed=embed)

#StatusredCommand
@bot.command() 
@commands.has_permissions(manage_messages = True)
async def Statusred(ctx):
  channel = bot.get_channel(805159215370076191)
  embed = discord.Embed(
    title = 'ZA FingerPrint Status', 
    description =  '',
    colour = discord.Colour.red()
  )
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name='**Status:**', value='\n **Some ZA FingerPrint Services are currently not Running. Don\'t worry. The team is busy working on a fix** 🔴 ', inline=True)
  await channel.send(embed=embed)

#Set Bot status
@tasks.loop(seconds=15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

#Discord Rules Embed
@bot.command() 
@commands.has_permissions(administrator = True)
async def Rules(ctx):
  embed = discord.Embed(
    title = 'ZaFingerPrint Server Rules', 
    description =  'Please Respect and Obey the Server',
    colour = discord.Colour.teal()
  )

  embed.set_footer(text='Made by MrT1TAN#3244')
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.set_author(name='MrT1TAN#3244', 
  icon_url='https://imgur.com/YoOQFrW.png')
  embed.add_field(name='Rule #1: **__NSFW Content__**', value='Any form of NSFW content is strictly forbidden, if you are found posting content of this nature, you will be banned on the spot.', inline=False)
  embed.add_field(name='Rule #2: **__Advertising__**', value='No advertising of any kind (Discord, YouTube, Twitter, Etc). If you are found advertising, this is also grounds for an immediate ban.', inline=False)
  embed.add_field(name='Rule #3: **__Defamation Behavior__**', value='Absolutely no Racist, Sexist, or otherwise degrading behavior will be tolerated. Anyone displaying this behavior will be banned.', inline=False)
  embed.add_field(name='Rule #4: **__Mentions__**', value='Repeated pings will result in a mute, kick, or even ban.', inline=False)
  embed.add_field(name='Rule #5: **__Discord Terms of Service__**', value='You must be at least 13 years old to use Discord, and raiding, illegal activities, attempting to obtain personal information, and all other prohibited acts will result in punishment.', inline=False)
  embed.add_field(name='Rule #6: **__Do not spam!__**', value='Avoid excessive and/or unnecessary messages, caps, emojis, text walls, spoiler messages, chains, images and @mentions. This includes unwarranted tags and derailing conversations.', inline=False)
  embed.add_field(name='Rule #7: **__Be respectful and accepting towards other members.__**', value='No instances of personal attacks, disrespect, exclusion, harassment, slurs, doxxing, or arguments should occur here. Treat everyone as if they\'re your equal. Don\'t try to act like a staff member or as if you have staffing ability if you don\'t have the role.', inline=False)


  msg = await ctx.send(embed=embed)
  await msg.add_reaction('<:agree:805537012161314816>')
bot.run('ODA1NDYxMzY4MDU1NTI5NTAy.YBbOWg.ga2Xakk4ddaD3m0x7sBN_UIn2GQ')