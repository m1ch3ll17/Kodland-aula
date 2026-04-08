import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"ola eu sou: {bot.user}")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')
