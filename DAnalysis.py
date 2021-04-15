import molarmass


def DA(command):
    starting_unit = command[3]

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

        return round(final_result, 3)

    elif desired_element == 'mol':
        final_result = desired_mol
        return round(final_result, 3)
