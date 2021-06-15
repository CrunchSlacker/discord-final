import math


class AssignVar:  # Figure this out BOY
    def __init__(self, command):
        self.command = command

    def return_var(self, elem_num):
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
                    elem_four = self.command[index].split('=')

        if elem_num == 1:
            return elem_one
        elif elem_num == 2:
            return elem_two
        elif elem_num == 3:
            return elem_three
        elif elem_num == 4:
            return elem_four


def no_x(command):
    elements = AssignVar(command)

    vf_elem = elements.return_var(1)
    vi_elem = elements.return_var(2)
    a_elem = elements.return_var(3)
    t_elem = elements.return_var(4)

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
    elements = AssignVar(command)

    x_elem = elements.return_var(1)
    vt_elem = elements.return_var(2)
    v0_elem = elements.return_var(3)
    t_elem = elements.return_var(4)

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
    elements = AssignVar(command)

    x_elem = elements.return_var(1)
    vo_elem = elements.return_var(2)
    t_elem = elements.return_var(3)
    a_elem = elements.return_var(4)

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
    elements = AssignVar(command)

    a_elem = elements.return_var(1)
    x_elem = elements.return_var(2)
    vt_elem = elements.return_var(3)
    v0_elem = elements.return_var(4)

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
