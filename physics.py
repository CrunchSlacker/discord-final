import math


class AssignVar:  # Figure this out BOY
    def __init__(self, command):
        self.command = command

    def get_var(self):
        elem_one = ""
        elem_two = ""
        elem_three = ""
        elem_four = ""

        index = -1
        for element in self.command:
            index = index + 1

            if "=" in element:
                if index == 1:
                    elem_one = self.command[index].split('=')
                elif index == 2:
                    elem_two = self.command[index].split('=')
                elif index == 3:
                    elem_three = self.command[index].split('=')
                elif index == 4:
                    elem_four = self.command[index].split('=')  #


def no_x(command):
    vf_elem = ""
    vi_elem = ""
    a_elem = ""
    t_elem = ""

    index = -1
    for element in command:
        index = index + 1

        if "=" in element:
            if index == 1:
                vf_elem = command[index].split('=')
            elif index == 2:
                vi_elem = command[index].split('=')
            elif index == 3:
                a_elem = command[index].split('=')
            elif index == 4:
                t_elem = command[index].split('=')

    vf_val = vf_elem[1]
    vi_val = vi_elem[1]
    a_val = a_elem[1]
    t_val = t_elem[1]

    if vf_val == "":
        v = float(vi_val) + (float(a_val) * float(t_val))
        return "vf = " + str(v)
    if vi_val == "":
        v0 = float(vf_val) / (float(a_val) * float(t_val))
        return "vi = " + str(v0)
    if a_val == "":
        a = (float(vf_val) - float(vi_val)) / float(t_val)
        return "a = " + str(a)
    if t_val == "":
        t = (float(vf_val) - float(vi_val)) / float(a_val)
        return "t = " + str(t)


def no_a(command):
    x_elem = ""
    vt_elem = ""
    v0_elem = ""
    t_elem = ""

    index = -1
    for element in command:
        index = index + 1

        if "=" in element:
            if index == 1:
                x_elem = command[index].split('=')
            elif index == 2:
                vt_elem = command[index].split('=')
            elif index == 3:
                v0_elem = command[index].split('=')
            elif index == 4:
                t_elem = command[index].split('=')

    x_val = x_elem[1]
    vt_val = vt_elem[1]
    v0_val = v0_elem[1]
    t_val = t_elem[1]

    if x_val == "":
        x = 0.5 * (float(vt_val) + float(v0_val)) * float(t_val)
        return "x = " + str(x)
    if vt_val == "":
        vt = 2 * (float(x_val) / float(t_val)) - float(v0_val)
        return "vt = " + str(vt)
    if v0_val == "":
        v0 = 2 * (float(x_val) / float(t_val)) - float(vt_val)
        return "v0 = " + str(v0)
    if t_val == "":
        t = (2 * float(x_val)) / (float(vt_val) + float(v0_val))
        return "t = " + str(t)


def no_vf(command):
    x_elem = ""
    vo_elem = ""
    t_elem = ""
    a_elem = ""

    index = -1
    for element in command:
        index = index + 1

        if "=" in element:
            if index == 1:
                x_elem = command[index].split('=')
            elif index == 2:
                vo_elem = command[index].split('=')
            elif index == 3:
                t_elem = command[index].split('=')
            elif index == 4:
                a_elem = command[index].split('=')

    x_val = x_elem[1]
    vo_val = vo_elem[1]
    t_val = t_elem[1]
    a_val = a_elem[1]

    if x_val == "":
        x = (float(vo_val) * float(t_val)) + (0.5 * float(a_val) * pow(float(t_val), 2))
        return "x = " + str(x)
    if vo_val == "":
        vo = ((2 * float(x_val)) - (float(a_val) * pow(float(t_val), 2))) / (2 * float(t_val))
        return "vo = " + str(vo)
    if t_val == "":
        t = (-float(vo_val) + math.sqrt(2 * float(a_val) * float(x_val) + pow(float(vo_val), 2)))
        return "t = " + str(t)
    if a_val == "":
        a = ((2 * float(x_val)) - (2 * float(vo_val) * float(t_val)))
        return "a = " + str(a)


def no_t(command):
    a_elem = ""
    x_elem = ""
    vt_elem = ""
    v0_elem = ""

    index = -1
    for element in command:
        index = index + 1

        if "=" in element:
            if index == 1:
                a_elem = command[index].split('=')
            elif index == 2:
                x_elem = command[index].split('=')
            elif index == 3:
                vt_elem = command[index].split('=')
            elif index == 4:
                v0_elem = command[index].split('=')

    a_val = a_elem[1]
    x_val = x_elem[1]
    vt_val = vt_elem[1]
    v0_val = v0_elem[1]

    if a_val == "":
        a = ((pow(float(vt_val), 2) - pow(float(v0_val), 2)) / (2 * float(x_val)))
        return "a = " + str(a)
    if x_val == "":
        x = ((pow(float(vt_val), 2) - pow(float(v0_val), 2)) / (2 * float(a_val)))
        return "x = " + str(x)
    if vt_val == "":
        vt = math.sqrt((2 * float(a_val) * float(x_val)) + pow(float(v0_val), 2))
        return "vt = " + str(vt)
    if v0_val == "":
        v0 = math.sqrt((-2 * float(a_val) * float(x_val)) + pow(float(vt_val), 2))
        return "v0 = " + str(v0)


def solve_equation(command):
    print(command)
    if 'v' in command[1]:
        return no_x(command)
    elif 'x' in command[1]:
        if 'vt' in command[2]:
            return no_a(command)
        elif 'vo' in command[2]:
            return no_vf(command)
    elif 'a' in command[1]:
        return no_t(command)
