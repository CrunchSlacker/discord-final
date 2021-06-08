def equation(command):
    print(command)

    v_var = ""
    v0_var = ""
    a_var = ""
    t_var = ""

    index = -1
    for element in command:
        index = index + 1

        if "=" in element:
            if index == 1:
                v_var = command[index].split('=')
            elif index == 2:
                v0_var = command[index].split('=')
            elif index == 3:
                a_var = command[index].split('=')
            elif index == 4:
                t_var = command[index].split('=')

    v_val = v_var[1]
    v0_val = v0_var[1]
    a_val = a_var[1]
    t_val = t_var[1]

    if v_var[1] == "":
        v = float(v_val) + (float(a_val) * float(t_val))
        return "v = " + str(v)
    if v0_var[1] == "":
        v0 = float(v_val) / (float(a_val) * float(t_val))
        return "v0 = " + str(v0)
    if a_var[1] == "":
        a = (float(v_val) - float(v0_val)) / float(t_val)
        return "a = " + str(a)
    if t_var[1] == "":
        t = (float(v_val) - float(v0_val)) / float(a_val)
        return "t = " + str(t)

    print(v_var)
    print(v0_var)
    print(a_var)
    print(t_var)
