import discord
from discord.ext import commands
import os
import aiohttp
from replit import db

init_triggers = ["treat", "eat", "snack", "toy", "scratch", "scritch", "fish", "fishing", "food", "itchy", "cat", "meat"]

if "ready" not in db.keys():
  db["ready"] = True

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
    img_req = await session.get(os.environ['cat_api'])
    img_json = await img_req.json()
    fact_req = await session.get(os.environ['fact_api'])
    fact_json = await fact_req.json()

  embed = discord.Embed(title="Kitty~", color=discord.Color.from_rgb(241, 22, 101))
  embed.set_image(url=img_json['link'])
  embed.set_footer(text = fact_json['fact'])
  await ctx.send(embed=embed)

@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  msg = message.content
  if any(word in msg for word in init_triggers):
    await message.channel.send('Meooow!')
  await bot.process_commands(message)

bot.run(os.environ['TOKEN'])

