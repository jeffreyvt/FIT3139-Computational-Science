def int2bin(num):
    """
    Converts base 10 integer value to binary
    :param num: integer value in base 10
    :return: binary value of the input with the right sign
    """
    if num == "0":
        return "0"
    elif num == "-0":
        return "-0"
    else:
        num = int(num)
        output = ""
        if num < 0:
            neg = True
            num *= -1
        else:
            neg = False
        while num > 0:
            if num % 2 == 0:
                output += "0"
            else:
                output += "1"
            num //= 2
        if neg:
            return "-"+output[::-1]
        else:
            return output[::-1]


def decimal2bin(num):
    """
    converts the base 10 decimal value to binary
    :param num: base 10 decimal value
    :return: binary value for the input
    """
    output = ""
    for i in range(32):
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
    """
    Combines the decimal2bin and int2bin function.
    Converts any real number to binary
    :param num: real number in base 10
    :return: binary value of the input value
    """
    tmp = str(num).split(".")
    if len(tmp) > 1:
        i = tmp[0]
        d = float("0."+tmp[1])
        result = int2bin(i) + "." + decimal2bin(d)
    else:
        i = int(tmp[0])
        result = int2bin(i)
    print(result)

float2bin(11.1)