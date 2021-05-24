import discord
import DAnalysis
import os

from Chemistry import molarmass

client = discord.Client()  # Connects with discord


@client.event
async def on_ready():
    print("Bot is ready".format(client))  # Ready message


@client.event
async def on_message(message):

    command = message.content.split()

    if command[0] == "-molar":
        embedMolarM = discord.Embed(title=str(command[1]) + " のモル質量:", description=str(round(
        molarmass.calc_mass(command[1]), 2)), color=0x3498db)
        await message.channel.send(embed = embedMolarM)

    elif command[0] == "-DA":
        embedDA = discord.Embed(title="単位変換:", description=str(DAnalysis.DA(command)), color=0x3498db)
        await message.channel.send(embed = embedDA)


client.run("ODMxMDE1MjI2MjY2MDkxNTMx.YHPFPQ.J5kobr2fp6Kj9Wz5hZj7QMzp5WA")  # Token
