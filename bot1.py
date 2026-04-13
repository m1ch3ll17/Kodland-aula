import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def ajuda(ctx):
        await ctx.send("""
📌 Lista de Comandos do Bot

👋 hello
→ Eu apenas digo olá e informo meu nome.

👋 bye
→ Envio um emoji para me despedir de você.

😂 heh [número]
→ Quanto maior o número, mais eu vou rir!

📅 joined @usuário
→ Mostra há quanto tempo a pessoa mencionada está no servidor.

🎲 roll NdN
→ Rola dados no formato RPG.
Exemplo: $roll 1d6 (1 dado com 6 lados)

---
💡 Use os comandos com o prefixo $
""")

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

@bot.command()
async def roll(ctx, dice: str):
    """Rola dados em formado NdN"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send("Não esta em formato NdN")
        return
    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
bot.run("T")
