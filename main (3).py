def rot(num):
    decomposition = []
    num = str(num)
    for digit in num:
        decomposition.append(int(digit))
    for i in range(len(decomposition)):
        if decomposition[i] == 6:
            decomposition[i] = 9
            break
    return int(''.join(map(str, decomposition)))


