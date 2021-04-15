import discord
import molarmass
import DAnalysis
import os

client = discord.Client()


@client.event
async def on_ready():
    print(
        "So this is where Enterprise is... A-ahem! I am Essex, one of the Union's state-of-the-art aircraft carriers. "
        "Commander, you can expect great things from me! I swear that I won't disappoint you!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-e'):
        command = message.content.split()

        if command[1] == "molarM":
            embed_molar_m = discord.Embed(title=str(command[2]) + " のモル質量:",
                                          description=str(round(molarmass.calc_mass(command[2]), 2)), color=0x3498db)
            embed_molar_m.set_thumbnail(url='https://media.tenor.com/images/dfa3ed17c46d7a679b5d2b4ae9fdca61/tenor.gif')
            await message.channel.send(embed=embed_molar_m)

        if command[1] == "DA":
            await message.channel.send(DAnalysis.DA(command))

        else:
            await message.channel.send("有効な入力ではありません、やり直してください。")


client.run('ODMxMTk3Nzc1MDg5MzY5MTA1.YHRvQA.hraUmwO2yoVfG8ekKh1NwAb4-ek')
