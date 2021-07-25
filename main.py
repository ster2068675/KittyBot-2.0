import discord
from discord.ext import commands
import os
import aiohttp

bot = commands.Bot(command_prefix="!", case_insensitive=True)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
  await ctx.send(f"Hello {ctx.author.name}!")

@bot.command()
async def cat(ctx):
  async with aiohttp.ClientSession() as session:
    req = await session.get('cat_api')
    json = await req.json()

bot.run(os.environ['TOKEN'])

