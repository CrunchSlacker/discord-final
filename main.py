import discord
import molarmass
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
            await message.channel.send("モル質量: " + str(round(molarmass.calc_mass(command[2]), 2)))

        else:
            await message.channel.send("有効な入力ではありません、やり直してください。")

client.run(os.environ['DISCORD_TOKEN'])
