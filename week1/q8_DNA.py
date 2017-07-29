def complement(string):
    output = ""
    for char in string:
        if char == "A":
            output += "T"
        elif char == "T":
            output += "A"
        elif char == "G":
            output += "C"
        elif char == "C":
            output += "G"
    return output


##incomplete