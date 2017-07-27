def int2bin(num):
    if num == 0:
        return 0
    else:
        output = ""
        while num > 0:
            if num % 2 == 0:
                output += "0"
            else:
                output += "1"
            num //= 2
        return output[::-1]


def decimal2bin(num):
    output = ""
    for i in range(10):
        num *= 2
        if num > 1:
            output += "1"
            num -= 1
        else:
            output += "0"
    return output


def float2bin(num):
    i, d = divmod(num, 1)
    result = int2bin(int(i)) + "." + decimal2bin(d)
    print(result)

float2bin(10.11)