

def subnet_divide(mask, subnets):
    addresses = 2 ** (32 - mask)
    output = []
    for i in range(subnets):
        if int(i*(addresses/subnets)) + 1 < 256:
            output.append(f'Подсеть {i}: 192.168.0.{int(i*(addresses/subnets)) + 1}')
        else:
            output.append(f'Подсеть {i}: 192.168.1.{int(i*(addresses/subnets)) + 1 - 256}')
    return output


