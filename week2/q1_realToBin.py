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
        if num >= 1:
            output += "1"
            num -= 1
        else:
            output += "0"
        if abs(num - 0.0) < 0.01:
            break
    return output


def float2bin(num):
    tmp = str(num).split(".")
    if len(tmp) > 1:
        i = int(tmp[0])
        d = float("0."+tmp[1])
        # print(i, d)
        result = int2bin(i) + "." + decimal2bin(d)
    else:
        i = int(tmp[0])
        result = int2bin(i)
    print(result)

float2bin(10.1)