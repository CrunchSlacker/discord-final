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

    if message.content.startswith('-e'):
        command = message.content.split()

        if command[1] == "molarM":
            embedMolarM = discord.Embed(title=str(command[2]) + " のモル質量:", description=str(round(
            molarmass.calc_mass(command[2]), 2)), color=0x3498db)
            await message.channel.send(embed = embedMolarM)

        elif command[1] == "DA":
            embedDA = discord.Embed(title="単位変換:", description=str(DAnalysis.DA(command)), color=0x3498db)
            await message.channel.send(embed = embedDA)

        else:
            await message.channel.send("Invalid Command")


client.run(os.environ['RICHARD_TOKEN'])  # Token
