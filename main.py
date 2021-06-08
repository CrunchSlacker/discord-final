import discord
import DAnalysis
import physics
import os

from Chemistry import molarmass

client = discord.Client()  # Connects with discord


@client.event
async def on_ready():
    print("Bot is ready".format(client))  # Ready message


@client.event
async def on_message(message):
    command = message.content.split()

    if command[0] == "-option":
        optionsList = discord.Embed(title="Options", description=str("Molar Mass Calculator: \n-molar ["
                                                                     "element/compound] \n ex. -molar H2SO4 \n\n "
                                                                     "Dimensional Analysis: \n "
                                                                     " -DA [amount] [unit] [e/c] [m ratio] [resulting "
                                                                     "unit] [e/c] \n ex. -DA 12.5 g Cu2S 1:2 g Cu "
                                                                     "\n\n Celsius to Kelvin Conversion: \n -k ["
                                                                     "celsius] \n ex. -k 69.8"), color=0x3498db)
        await message.channel.send(embed=optionsList)

    if command[0] == "-molar":
        embedMolarM = discord.Embed(title=str(command[1]) + " のモル質量:", description=str(round(
            molarmass.calc_mass(command[1]), 2)), color=0x3498db)
        await message.channel.send(embed=embedMolarM)

    elif command[0] == "-da":
        embedDA = discord.Embed(title="単位変換:", description=str(DAnalysis.DA(command)), color=0x3498db)
        await message.channel.send(embed=embedDA)

    elif command[0] == "-k":
        kelvin = float(command[1]) + 273
        embedKelvin = discord.Embed(title="ケルビンから摂氏へ換算:", description=str(kelvin), color=0x3498db)
        await message.channel.send(embed=embedKelvin)

    elif command[0] == "-kinematics":
        embedKinematics = discord.Embed(title="運動方程式:", description=str(physics.equation(command)), color=0x3498db)
        await message.channel.send(embed=embedKinematics)


client.run('ODMxMDE1MjI2MjY2MDkxNTMx.YHPFPQ.J5kobr2fp6Kj9Wz5hZj7QMzp5WA')  # Token
