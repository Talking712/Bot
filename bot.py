import discord
from discord.ext import commands


intents = discord.Intents.all()

bot = commands.Bot (command_prefix=':', intents = intents)

@bot.event
async def on_ready():
    print("*online*")

bot.run("Token")
