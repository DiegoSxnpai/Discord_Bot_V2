# bot.py
import discord
from discord.ext import commands, tasks

bot_token = 'MTIwMDgzNzQ3MzM1MDIwNTUxMA.GM9TGe.iFg5Z4vfzYyoC9vSwk6TR-gW0yw6X-gWCwIFWY'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(seconds=1)
async def check_bot_ready():
    if bot.is_ready():
        check_bot_ready.stop()
        await on_ready()

async def start_bot():
    check_bot_ready.start()
    await bot.start(bot_token)

async def stop_bot():
    await bot.close()

@bot.event
async def on_message(message):
    if message.content.startswith('!stopbot'):
        await stop_bot()

# rest of your bot code

