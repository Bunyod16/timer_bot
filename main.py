import os
from unittest.util import _count_diff_all_purpose
from discord.ext import commands, tasks
from numpy import diff
import pytz
from datetime import datetime, timezone, tzinfo
import math

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi', help_command=None)
TIMER_CHANNEL_ID = 950107282438516807
GUILD_ID = 892149669084401705
start = 0
def get_token():
  token = os.getenv("TOKEN")
  return (token)

@bot.event
async def on_ready():
    print(bot.user.name, "is online")
    print(bot.user.id)
    timed_checker.start()

def get_remaining_time(info):
    current_time = datetime.now(tz=timezone.utc)
    target_time = datetime.strptime(
			info, "%d/%m/%Y %H:%M").replace(tzinfo=timezone.utc)
    print(current_time, target_time)
    difference =(target_time - current_time)
    seconds = difference.total_seconds()
    minutes = seconds / 60
    hours = math.floor(minutes / 60)
    minutes = math.floor(minutes - (hours * 60))
    days = math.floor(hours / 24)
    if (days >= 1):
        hours += (days * 24)
    if (hours < 0 or minutes < 0):
        hours = 0
        minutes = 0
    return ({"hours":hours,"minutes":minutes})



finish_time = "07/03/2022 18:00"

@tasks.loop(minutes=5)
async def timed_checker():
  time_remaining = get_remaining_time(finish_time)
  auction_channel = bot.get_channel(TIMER_CHANNEL_ID)
  time = f"mint-{time_remaining['hours']}h-{time_remaining['minutes']}m"
  print(time_remaining)
  await auction_channel.edit(name = time)

bot.run(get_token())