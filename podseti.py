

def subnet_divide(mask, subnets):
    addresses = 2 ** (32 - mask)
    output = []
    for i in range(subnets):
        output.append(f'Подсеть {i}: 192.168.{int(i*(addresses/subnets)) + 1// 256}.{int(i*(addresses/subnets)) + 1} % 256')
    return output


