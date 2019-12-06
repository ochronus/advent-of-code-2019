def simulate(data):
    ip = 0
    while data[ip] != 99:
        cur_i = int(str(data[ip])[-2:])
        param_modes = str(data[ip])[:-2]
        if cur_i == 1:
            data[data[ip + 3]] = get_param(
                param_modes, data, ip, 1) + get_param(param_modes, data, ip, 2)
            ip += 4
        if cur_i == 2:
            data[data[ip + 3]] = get_param(
                param_modes, data, ip, 1) * get_param(param_modes, data, ip, 2)
            ip += 4
        if cur_i == 3:
            data[data[ip + 1]] = int(input("Gimme input: "))
            ip += 2
        if cur_i == 4:
            print(get_param(param_modes, data, ip, 1))
            ip += 2
        if cur_i == 5:
            if (get_param(param_modes, data, ip, 1) != 0):
                ip = get_param(param_modes, data, ip, 2)
            else:
                ip += 3
        if cur_i == 6:
            if (get_param(param_modes, data, ip, 1) == 0):
                ip = get_param(param_modes, data, ip, 2)
            else:
                ip += 3
        if cur_i == 7:
            if (get_param(param_modes, data, ip, 1) < get_param(param_modes, data, ip, 2)):
                data[data[ip + 3]] = 1
            else:
                data[data[ip + 3]] = 0
            ip += 4
        if cur_i == 8:
            if (get_param(param_modes, data, ip, 1) == get_param(param_modes, data, ip, 2)):
                data[data[ip + 3]] = 1
            else:
                data[data[ip + 3]] = 0
            ip += 4

    return data


def get_param(param_modes, data, pointer, param):
    try:
        type = int(param_modes[-param])
    except IndexError:
        type =0
    if (type == 0):
        return data[data[pointer + param]]
    else:
        return data[pointer + param]


with open('../input.txt', 'r') as file:
    data = file.read().replace('\n', '')

instructions = [int(x) for x in data.split(',')]

simulate(instructions)
