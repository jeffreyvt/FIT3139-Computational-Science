def triangle_classifier(t1, t2, t3):
    angles = [t1, t2, t3]
    angles.sort()
    if angles[0] == 60 and angles[1] == 60:
        return "Equilateral"
    if angles[0] == angles[1] or angles[1] == angles[2]:
        return "Isosceles"
    else:
        return "Scalene"


if __name__ == "__main__":
    for i in range(1, 179):
        for j in range(1, 180 - i):
            k = 180 - i - j
            print(i, j, k, triangle_classifier(i, j, k))
