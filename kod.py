import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def choose(ctx, *choices):
    if len(choices) < 2:
        await ctx.send("En az iki seçenek belirtmelisiniz.")
    else:
        chosen = random.choice(choices)
        await ctx.send(f'Ben seçtim: {chosen}')
@bot.command()
async def mem(ctx):
    with open('more-the-merrier-31380-2webp','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memler(ctx): 
    image_name = random.choice(os.listdir('memler'))
    with open(f'memler/{image_name}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
@bot.command()
async def hayvanlar(ctx): 
    image_name = random.choice(os.listdir('hayvanlar'))
    with open(f'hayvanlar/{image_name}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
bot.run("TOKEN")
