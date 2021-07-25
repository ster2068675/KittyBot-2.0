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

@bot.command(name='kitty', description="sends a pic of a kitty to the chat")
async def kitty(ctx):
  async with aiohttp.ClientSession() as session:
    req = await session.get(os.environ['cat_api'])
    json = await req.json()
  embed = discord.Embed(title="Kitty~", color=discord.Color.from_rgb(241, 22, 101))
  embed.set_image(url=json['link'])
  await ctx.send(embed=embed)

bot.run(os.environ['TOKEN'])

