from pydoc import cli
import discord
from discord import message
from discord.ext import commands
import youtube_dl
import os
import asyncio
import random
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('TOKEN'))

token = str(os.getenv('TOKEN'))
client = commands.Bot(command_prefix="*")
client.inactive = False
global WaitTime 
number = 5
client.songs =[]


dir_path = os.path.dirname(os.path.realpath(__file__))
 
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            print (root+'/'+str(file))
            client.songs.append(file)


print(client.songs)
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
        lower
    if len(message.content) > 0:
        print(message.content)
        if "stop" in message.content:
            client.inactive = True
            print(client.inactive)
            await message.channel.send('Stopped')
        


@client.command(name='rndm', help='randomly joins and does a meme')
async def rndm(ctx, amount = '5'):
    client.inactive = False
    WaitTime = 10
    number = int(amount)
    Times = 1
    await ctx.send("Started!")
    voiceChannel = ctx.author.voice.channel
    while Times <= number:
        song = random.choice(client.songs)
        print(song)
        print(client.inactive)
        if Times == number:
            client.inactive = False
            await ctx.send("Stopped!")
        
        if client.inactive == True:
            await ctx.send("Stopped!")
            break
        print(WaitTime/60)
        print(WaitTime)
        for i in range(WaitTime):
            vc = ctx.author.voice.channel
            print(vc)
            if vc is None:
                await ctx.send("Stopped!")
                break
            print(WaitTime)
            print('i:'+ str(i))
            await asyncio.sleep(1)
        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(song))
        await asyncio.sleep(5)
        await voice.disconnect()
        WaitTime = random.randrange(60, 600)
        Times = Times + 1
    await ctx.send("Done!")




client.run(token)

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
