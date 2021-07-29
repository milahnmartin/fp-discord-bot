import time
import discord
import pyrebase
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle


# Set Prefix
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


# Gets Information from Firebase
config = {
    "apiKey": "AIzaSyDZpGc9E2BhD_XMJcYlir2c_bRVoL--hJw",
    "authDomain": "fingerprint-za.firebaseapp.com",
    "databaseURL": "https://fingerprint-za-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "fingerprint-za",
    "storageBucket": "fingerprint-za.appspot.com",
    "messagingSenderId": "1099288539318",
    "appId": "1:1099288539318:web:5944ddd1eb25e0b58c7617",
    "measurementId": "G-5L8EW2MW4R",
}


# Embedded Player info
@bot.command()
async def cs(ctx, player="ultrafy"):
    function_hit('cs')
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    rootRef = database.child("counterstrike/pro").get()
    data = rootRef.val()

    playerU = player.upper()

    # try:
    myplayer = data[playerU]
    # await ctx.send('Showing Results for ' + myplayer)
    keyboard = myplayer["keyboard"]
    mouse = myplayer["mouse"]
    age = myplayer["age"]
    fullname = myplayer["fullname"]
    headset = myplayer["headset"]
    resolution = myplayer["resolution"]
    monitor = myplayer["monitor"]
    monitor_hz = myplayer["monitor_hz"]
    raw_input = myplayer["raw_input"]
    sens = myplayer["sensitivity"]
    team = myplayer["team"]
    aspect_ratio = myplayer["aspect_ratio"]
    dpi = myplayer["dpi"]
    scaling_mode = myplayer["scaling_mode"]
    zoom_sens = myplayer["zoom_sens"]
    gamertag = myplayer["gamertag"]
    crosshair_code = myplayer["crosshair_code"]
    # faceit = myplayer['faceit']
    # esea = myplayer['esea']
    # except KeyError:
    # await ctx.send('User ' + myplayer + ' does not exist, contact support !')

    await ctx.send("Busy fetching fpdata!", delete_after=3.0)
    embed = discord.Embed(
        title="Player Information",
        description="All Available fpdata about the player is stated below.",
        colour=discord.Colour.teal(),
    )

    embed.set_footer(
        text="Website: https://fingerprintza.comblahsad/ | Twitter: @fingerprintza "
    )
    embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
    embed.add_field(name="**__Player:__**", value=gamertag, inline=False)
    embed.add_field(
        name="**__Player Information__**",
        value="**FullName:** "
        + fullname
        + "\n**Player Team:** "
        + team
        + "\n**Age:** "
        + age,
        inline=False,
    )
    embed.add_field(
        name="**__Mouse Settings__**",
        value="**DPI:** "
        + dpi
        + "\n**Sensitivity:** "
        + sens
        + "\n**Raw Input:** "
        + raw_input
        + "\n**Zoom Sensitivity:** "
        + zoom_sens,
        inline=False,
    )
    embed.add_field(
        name="**__Monitor Settings__**",
        value="**Resolution:** "
        + resolution
        + "\n**Aspect Ratio:** "
        + aspect_ratio
        + "\n**Scaling Mode:** "
        + scaling_mode
        + "\n**Hz:** "
        + monitor_hz,
        inline=False,
    )
    embed.add_field(
        name="**__Crosshair__**",
        value="**Crosshair Code:** " + crosshair_code,
        inline=False,
    )
    embed.add_field(
        name="**__Gear__**",
        value="**Monitor:** "
        + monitor
        + "\n**Mouse:** "
        + mouse
        + "\n**Keyboard:** "
        + keyboard
        + "\n**Headset:** "
        + headset,
        inline=False,
    )
    

    await ctx.send(embed=embed)


@bot.command()
async def fortnite(ctx, player="ultrafy"):
    function_hit('fortnite')
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    rootRef = database.child("fortnite/pro").get()
    data = rootRef.val()

    playerU = player.upper()

    # try:
    myplayer = data[playerU]
    # await ctx.send('Showing Results for ' + myplayer)
    keyboard = myplayer["keyboard"]
    mouse = myplayer["mouse"]
    age = myplayer["age"]
    fullname = myplayer["fullname"]
    headset = myplayer["headset"]
    resolution = myplayer["resolution"]
    monitor = myplayer["monitor"]
    monitor_hz = myplayer["monitor_hz"]
    color_blind_mode = myplayer["color_blind_mode"]
    sens = myplayer["sensitivity"]
    team = myplayer["team"]
    vsyncc = myplayer["vsyncc"]
    dpi = myplayer["dpi"]
    brightness = myplayer["brightness"]
    scope_sens = myplayer["scope_sens"]
    gamertag = myplayer["gamertag"]
    fortnite_tracker = myplayer["fortnite_tracker"]
    # binds
    ramp_bind = myplayer["ramp_bind"]
    wall_bind = myplayer["wall_bind"]
    cone_bind = myplayer["cone_bind"]
    edit_bind = myplayer["edit_bind"]
    floor_bind = myplayer["floor_bind"]
    edit_release = myplayer["edit_release"]
    # faceit = myplayer['faceit']
    # esea = myplayer['esea']
    # except KeyError:
    # await ctx.send('User ' + myplayer + ' does not exist, contact support !')

    await ctx.send("Busy fetching fpdata!", delete_after=3.0)
    embed = discord.Embed(
        title="Player Information",
        description="All Available fpdata about the player is stated below.",
        colour=discord.Colour.teal(),
    )

    embed.set_footer(
        text="Website: https://fingerprintza.com/ | Twitter: @fingerprintza "
    )
    embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
    embed.add_field(name="**__Player:__**", value=gamertag, inline=False)
    embed.add_field(
        name="**__Player Information__**",
        value="**FullName:** "
        + fullname
        + "\n**Player Team:** "
        + team
        + "\n**Age:** "
        + age,
        inline=False,
    )
    embed.add_field(
        name="**__Mouse Settings__**",
        value="**DPI:** "
        + dpi
        + "\n**Sensitivity:** "
        + sens
        + "\n**Scope Sensitivity:** "
        + scope_sens,
        inline=False,
    )
    embed.add_field(
        name="**__Monitor Settings__**",
        value="**Resolution:** "
        + resolution
        + "\n**Color Blind Mode:** "
        + color_blind_mode
        + "\n**Brightness:** "
        + brightness
        + "\n**Hz:** "
        + monitor_hz,
        inline=False,
    )
    embed.add_field(
        name="**__Fortnite Binds__**",
        value="**Ramp Bind:** "
        + ramp_bind
        + "\n**Cone Bind:** "
        + cone_bind
        + "\n**Floor Bind:** "
        + floor_bind
        + "\n**Wall Bind:** "
        + wall_bind,
        inline=False,
    )
    embed.add_field(
        name="**__Gear__**",
        value="**Monitor:** "
        + monitor
        + "\n**Mouse:** "
        + mouse
        + "\n**Keyboard:** "
        + keyboard
        + "\n**Headset:** "
        + headset,
        inline=False,
    )
    embed.add_field(
        name="**__Sponsors: __** ",
        value="- Tint Formulae | #FindYourHiddenEnergy | Use code fingerprint for 5"
        + "%"
        + " off \n - FrostByte Network | @FrostByteZA",
        inline=False,
    )

    await ctx.send(embed=embed)


@bot.command()
async def counterstrikers(ctx):
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    rootRef = database.child("counterstrike/pro").get()
    data = rootRef.val()
    await ctx.send("Getting Players!", delete_after=3.0)
    await ctx.send("***Players :***")
    for i in data:
        await ctx.send("`" + i + "`")
        time.sleep(2)


@bot.command()
async def fortniters(ctx):
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    rootRef = database.child("fortnite/pro").get()
    data = rootRef.val()
    await ctx.send("Getting Players!", delete_after=3.0)
    await ctx.send("***Players :***")
    for i in data:
        await ctx.send("`" + i + "`")
        time.sleep(2)


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
        name="**__.counterstrikers:__**",
        value="Shows All CS Players In Database",
        inline=False,
    )
    embed.add_field(
        name="**__.fortniters:__**",
        value="Shows All Fortnite Players In Database",
        inline=False,
    )
    embed.add_field(
        name='**__.fortnite + "player name"__**',
        value="Shows Fortnite Player Specified After .fortnite Info",
        inline=False,
    )
    embed.add_field(
        name='**__.cs + "player name"__**',
        value="Shows CS Player Specified After .cs Info",
        inline=False,
    )
    embed.add_field(
        name="**__.clear__** + **__amount__**",
        value="Clears Specific amount of lines",
        inline=False,
    )

    await ctx.send(embed=embed)



# Purge command
@bot.command(aliases=["p", "purge", "delete"])
async def clear(ctx, amount=3):
    function_hit('clear')
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title="FingerPrintZa",
        description="FingerPrintZa Bot Cleared: "
        + "`"
        + str(amount)
        + "`"
        + " messages"
        + emojiF,
        colour=discord.Colour.teal(),
    )
    await ctx.send(embed=embed, delete_after=3.0)





@bot.command()
async def invite(ctx):
    function_hit('invite')
    embed = discord.Embed(
        title="ZA FingerPrint Status",
        description="Invite link to invite the bot to your server",
        colour=discord.Colour.teal(),
    )
    embed.set_footer(
        text="Website: https://fingerprintza.com/ | Twitter: @fingerprintza"
    )
    embed.set_thumbnail(url="https://imgur.com/P1msmYz.png")
    embed.add_field(
        name="**Invite Link:**",
        value="\n **https://discord.com/api/oauth2/authorize?client_id=805461368055529502&permissions=0&scope=bot** ",
        inline=True,
    )
    await ctx.send(embed=embed)




# Set Bot status
@tasks.loop(seconds=15)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))



def function_hit(information:str)->None:
    print("Command ", information, " Was Hit !")



bot.run("ODA1NDYxMzY4MDU1NTI5NTAy.YBbOWg.ga2Xakk4ddaD3m0x7sBN_UIn2GQ")
