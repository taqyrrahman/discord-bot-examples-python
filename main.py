from discord.ext import commands
import nest_asyncio
import aiocron
import discord
import apis

token = "YOUR_TOKEN"

# needed to be able run synchronous functions
nest_asyncio.apply()

# prefix for the commands
bot = commands.Bot(command_prefix="$")


# what to do when the bot is ready
@bot.event
async def on_ready():
    # to show the bot is playing Cyberpuke 2021
    await bot.change_presence(activity=discord.Game(name="Cyberpuke 2021"))
    print("Bot connected as {}".format(bot.user))


# cron (every hour) at minute 0, you can change the expression
# some references about cron = https://crontab.guru/
# you can change the name as you wish
@aiocron.crontab("0 * * * *")
async def every_hour():
    try:
        # add your own channel id
        some_channel = 0
        channel: discord.TextChannel = bot.get_channel(some_channel)
        # send cat facts
        await channel.send(apis.get_cat_facts())
    except Exception as e:
        # show the error if any
        print(e)


# what to do when a message coming
@bot.event
async def on_message(msg: discord.Message):
    # make sure the bot dont process its own message
    if msg.author == bot.user:
        return

    # dont forget to add this to make the bot process the commands if any
    await bot.process_commands(msg)


# if someone send a message "$hey"
# prefix configured at the start ($)
@bot.command()
async def hey(ctx: commands.Context, *args):
    # msg: discord.Message => to mark a msg as discord.Message
    msg: discord.Message = ctx.message

    # on windows 10 just press win + ;
    # then select the emoji, dont forget to wrap it with "" or ''
    await msg.add_reaction("❤")

    # or you could use it like this
    emoji = "\U0001F44D"
    await msg.add_reaction(emoji)


# if someone send a message "$cat_facts"
@bot.command()
async def cat_facts(ctx: commands.Context, *args):
    try:
        result = apis.get_cat_facts()

        # to send a message as a reply
        # await ctx.reply(result)

        # to send a normal message
        await ctx.send(result)
    except Exception as e:
        print(e)


# make sure the codes above this line
bot.run(token)
