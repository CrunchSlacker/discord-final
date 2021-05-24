import math

import Sfig
from Chemistry import molarmass

#-DA 5.95 g CO2 1:1 g PbCO3

def DA(command):
    starting_unit = command[2]
    starting_mol = command[1]

    desired_unit = command[-2]
    desired_element = command[-1]

    if starting_unit == 'g':  # Change grams to mols
        starting_mol = float(command[1]) / molarmass.calc_mass(command[3])
        print(starting_mol)
    elif starting_unit == 'mol':
        starting_mol = command[1]

    if ":" in command[4]:
        ratio = command[4].split(':')

        desired_mol = float(starting_mol) * (int(ratio[1]) / int(ratio[0]))

        if desired_unit == 'mol':
            final_result = desired_mol
            sigfig = find_sigfigs(command[1])
            #final_result_sigfig = round(final_result, sigfig - int(math.floor(math.log10(abs(final_result)))) - 1)
            #number = f'{final_result_sigfig:.2f}'
            #print(number[-1])
            #if number[-1] == "0":
                #return f'{final_result_sigfig:.2f}'
            #else:
                #return str(Sfig.SF(final_result, sigfig)) + desired_unit + " of " + desired_element
            #return str(Sfig.SF(final_result, sigfig)) + desired_unit + " of " + desired_element
            print(final_result)
            return final_result

        elif desired_unit == 'g':
            final_result = desired_mol * molarmass.calc_mass(desired_element)
            sigfig = find_sigfigs(command[1])
            #print(final_result)
            #final_result_sigfig = round(final_result, sigfig - int(math.floor(math.log10(abs(final_result)))) - 1)
            #number = f'{final_result_sigfig:.2f}'
            #print(number[-1])
            #if number[-1] == "0":
                #return f'{final_result_sigfig:.2f}'
            #else:
                #return str(Sfig.SF(final_result, sigfig)) + desired_unit + " of " + desired_element
            #str(Sfig.SF(final_result, sigfig)) + desired_unit + " of " + desired_element
            print(final_result)
            return final_result


"""
Beginning of cited code
https://stackoverflow.com/questions/8142676/python-counting-significant-digits
"""


def find_sigfigs(x):
    """Returns the number of significant digits in a number. This takes into account
       strings formatted in 1.23e+3 format and even strings such as 123.450"""
    # change all the 'E' to 'e'
    x = x.lower()
    if 'e' in x:
        # return the length of the numbers before the 'e'
        myStr = x.split('e')
        return len(myStr[0]) - 1  # to compensate for the decimal point
    else:
        # put it in e format and return the result of that
        # NOTE: because of the 8 below, it may do crazy things when it parses 9 sigfigs
        n = ('%.*e' % (8, float(x))).split('e')
        # remove and count the number of removed user added zeroes. (these are sig figs)
        if '.' in x:
            s = x.replace('.', '')
            # number of zeroes to add back in
            l = len(s) - len(s.rstrip('0'))
            # strip off the python added zeroes and add back in the ones the user added
            n[0] = n[0].rstrip('0') + ''.join(['0' for num in range(l)])
        else:
            # the user had no trailing zeroes so just strip them all
            n[0] = n[0].rstrip('0')
        # pass it back to the beginning to be parsed
    return find_sigfigs('e'.join(n))


"""End of cited code"""
