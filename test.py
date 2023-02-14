def checkbase(base):
    i = 0
    while i < len(base):
        if base[i] == '+' or base[i] == '-':
            return 0
        if base.count(base[i]) > 1:
            return 0
        i += 1
    if i < 2:
        return 0
    return 1


def atoi_base(number, from_base):
    sign = 1
    if '-' in number:
        sign = -1
    result = 0

    for i in number:
        current = from_base.index(i)
        result = result * 10 + current

    print('atoi_base done')
    return result * sign


def convert_base(number, to_base):
    arr = ''
    sign = 0
    if number < 0:
        sign = 1
    while True:
        arr += to_base[number % len(to_base)]
        number = int(number / len(to_base))
        if number == 0:
            break
    if (sign == 1):
        arr += '-'
    arr = arr[::-1]
    print('convert_base done')
    return arr


result = atoi_base('-2147483647', '0123456789')
res2 = convert_base(result, '01')
print(res2)
