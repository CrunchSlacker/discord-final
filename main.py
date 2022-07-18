import discord
import DAnalysis
import physics
import random
import benis
from Chemistry import molarmass

client = discord.Client()  # Connects with discord


@client.event
async def on_ready():
    print("Bot is ready".format(client))  # Ready message


@client.event
async def on_message(message):
    command = message.content.split()

    try:
        if command[0] == "-molar":
            try:
                embedMolarM = discord.Embed(title=str(command[1]) + " のモル質量:", description=str(round(
                    molarmass.calc_mass(command[1]), 2)), color=0x3498db)
                await message.channel.send(embed=embedMolarM)
            except SystemExit:
                unknown_elem = discord.Embed(title=str("エラー、やり直してください"), color=0x3498db)
                await message.channel.send(embed=unknown_elem)

        elif command[0] == "-da":
            embedDA = discord.Embed(title="単位変換:", description=str(DAnalysis.DA(command)), color=0x3498db)
            await message.channel.send(embed=embedDA)

        elif command[0] == "-k":
            kelvin = float(command[1]) + 273
            embedKelvin = discord.Embed(title="ケルビンから摂氏へ換算:", description=str(kelvin), color=0x3498db)
            await message.channel.send(embed=embedKelvin)

        elif command[0] == "-kinematics":
            embedKinematics = discord.Embed(title="運動方程式:", description=str(physics.solve_equation(command)),
                                            color=0x3498db)
            await message.channel.send(embed=embedKinematics)

        elif command[0] == "-options":
            optionsList = discord.Embed(title="オプション", description=str("モル質量電卓\n -molar [元素/化合物]\n 例: -molar H2SO4\n\n"
                                                                       "単位変換\n -da [番号] [測定単位] [化合物] [モル比] [測定単位] [化合物]\n 例: -da 12.5 g Cu2S 1:2 g Cu\n\n"
                                                                       "ケルビンから摂氏へ換算\n -k [摂氏]\n 例: -k 72.3\n"), color=0x3498db)

            await message.channel.send(embed=optionsList)

        elif command[0] == "-benis":
            random_num = random.randint(0, 4)
            await message.channel.send(benis.gif_list[random_num])

    except IndexError:
        pass


client.run('ODMxMDE1MjI2MjY2MDkxNTMx.G-DL3e.Z73A0vHqhc0iwYNm_4CTAQ2qHDgi3_-gqrhJP4')  # Token
