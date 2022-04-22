from pydoc import cli
import discord
from discord import message
from discord.ext import commands
import youtube_dl
import os
import asyncio
import random
token = ''
client = commands.Bot(command_prefix="*")
client.songs = ["awaawa.mp3","dababyletsgo.mp3","kerstboom.mp3","okayletsgo.mp3"]
client.inactive = False
global WaitTime 
number = 5

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
        lower
    if len(message.content) > 0:
        print(message.content)
        if "stop" in message.content:
            print("INACTIVE")
            client.inactive = True
            print(client.inactive)
            await message.channel.send('Stopped the random meme!!')
        


@client.command()
async def rndm(ctx):
    client.inactive = False
    WaitTime = 10
    Times = 1
    await ctx.send("Started!")
    voiceChannel = ctx.author.voice.channel
    while Times <= number:
        song = random.choice(client.songs)
        print(song)
        print(client.inactive)
        if Times == number:
            client.inactive = False
            print('done')
        
        if client.inactive == True:
            print("stopped")
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
        #song_there = os.path.isfile("awaawa.mp3")
        #try:
        #    if song_there:
        #        'os.remove("song.mp3")'
        #except PermissionError:
        #    await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        #    return

        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        '''with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")'''
        voice.play(discord.FFmpegPCMAudio(song))
        await asyncio.sleep(5)
        await voice.disconnect()
        WaitTime = random.randrange(60, 600)
        Times = Times + 1




client.run(token)

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
