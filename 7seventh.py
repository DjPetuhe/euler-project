def prostoe(x):
    if (x == 2):
        return True
    if (x <= 1):
        return False
    for j in range(2, x):
        if (x % j == 0):
            return False
    else:
        return True


i = 0
x = 0
while (i != 10001):
    x += 1
    if prostoe(x):
        i += 1
print(x)
