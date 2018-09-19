import asyncio
import random
import json
import os
import discord

#TheTighties & Affidavid
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('mobat'):
        command = message.content[6:]
        switcher = {
            "about": "This is a discord bot to provide the user with statistics of their account with the chosen MOBA.",
            "help": "MOBA-t commands are:\nabout and help."
        }
        await client.send_message(message.channel, switcher.get(command, "Invalid command. Type 'mobat help' for list of commands."))

client.run('Your Code Here') 
client.close()
