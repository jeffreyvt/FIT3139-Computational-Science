import numpy as np

def distance(s1, s2):
    s1_L = len(s1)
    s2_L = len(s2)
    table = np.array([[-1 for _ in range(s1_L+1)] for _ in range(s2_L+1)])
    for i in range(s1_L+1):
        table[0][i] = i
    for j in range(s2_L+1):
        table[j][0] = j
    # print(table)

    # compute edit distance
    for i in range(1, s2_L+1):
        for j in range(1, s1_L+1):
            if s1[j-1] == s2[i-1]:
                s = 0
            else:
                s = 1
            table[i][j] = min(table[i-1][j-1]+s, table[i-1][j]+1, table[i][j-1]+1)
    print(table)
    print(table[s2_L][s1_L])


distance("DENTSGNAWSTRIMS","DNASGIVETHIS")