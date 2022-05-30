# bot.py
import os

import discord

TOKEN = "OTgwMzM5NTYxOTAzMzA0NzI0.GtmUW_.3d9nMAurhZjQh832noAqEWLpuZJ8ZZbP2pWBIQ"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("Hello from the other side!")


client.run(TOKEN)
