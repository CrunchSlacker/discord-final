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
            embed_molar_m = discord.Embed(title=str(command[2]) + " のモル質量:",
                                          description=str(round(molarmass.calc_mass(command[2]), 2)), color=0x3498db)
            embed_molar_m.set_thumbnail(url='https://media.tenor.com/images/dfa3ed17c46d7a679b5d2b4ae9fdca61/tenor.gif')
            await message.channel.send(embed=embed_molar_m)
        else:
            await message.channel.send("有効な入力ではありません、やり直してください。")

        if command[1] == "DA":

            starting_unit = command[3]


            mol_ratio = False

            desired_unit = command[-2]
            desired_element = command[-1]

            if ":" in command[5]:
                ratio = command[5].split(':')
                mol_ratio = True
            else:
                mol_ratio = False

            if starting_unit == 'g':  # Convert grams to mol
                starting_mol = round(float(command[2]) / molarmass.calc_mass(command[4]), 2)

            if mol_ratio:  # Multiply by mol ratio (if any)
                desired_mol = starting_mol * (int(ratio[0]) / int(ratio[1]))
                print(desired_mol)

            if desired_unit == 'g':  # Converts from mols to grams
                if not mol_ratio:
                    final_result = starting_mol * molarmass.calc_mass(desired_element)

                if mol_ratio:
                    final_result = desired_mol * molarmass.calc_mass(desired_element)

                await message.channel.send(round(final_result, 3))

            elif desired_element == 'mol':
                final_result = desired_mol
                await message.channel.send(round(final_result, 3))
        else:
            await message.channel.send("有効な入力ではありません、やり直してください。")


client.run('ODMxMTk3Nzc1MDg5MzY5MTA1.YHRvQA.hraUmwO2yoVfG8ekKh1NwAb4-ek')
