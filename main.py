import discord
import Chemistry.molarmass
import Chemistry.DAnalysis
import os

client = discord.Client()  # Connects with discord


@client.event
async def on_ready():
    print("Bot is ready".format(client))  # Ready message


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # If discord message begins with -e, then execute molar mass / DA command
    if message.content.startswith('-e'):
        command = message.content.split()

        # Calculates molar mass and sends to user
        if command[1] == "molarM":
            embed_molar_m = discord.Embed(title=str(command[2]) + " molar mass:",
                                          description=str(round(Chemistry.molarmass.calc_mass(command[2]), 2)),
                                          color=0x3498db)

            await message.channel.send(embed=embed_molar_m)

        # Calculates DA of specified elements and sends to user
        elif command[1] == "DA":
            da_embed_title = command[2] + command[3] + " of " + command[4] + " to " + command[-1] + "(" + command[
                2] + ")"
            embed_da = discord.Embed(title=da_embed_title, description=Chemistry.DAnalysis.DA(command), colour=0x3498db)
            await message.channel.send(embed=embed_da)

        else:
            await message.channel.send("Invalid Command")


client.run(os.environ['DISCORD_TOKEN'])  # Token
