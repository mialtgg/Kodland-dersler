import discord
from discord.ext import commands

# Botu oluşturuyoruz
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğine erişim izni
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot başladığında çalışacak kod
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

# Basit bir komut ekleyelim
@bot.command()
async def hello(ctx):
    await ctx.send("Merhaba, uzaylııı👽")

# Botu başlatıyoruz
bot.run('YOUR_BOT_TOKEN') 