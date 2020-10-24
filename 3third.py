from math import sqrt


def prostoe(x):
    if (x == 1 or x == 2):
        return True
    if (x <= 0):
        return False
    for j in range(2, x):
        if (x % j == 0):
            return False
    else:
        return True


def main():
    i = int(sqrt(600851475143))
    while (i != 0):
        if (600851475143 % i == 0 and prostoe(i)):
            print(i)
            quit()
        i -= 1


main()
