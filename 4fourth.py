def palindrom(number):
    number = str(number)
    return (number == number[::-1])


maximum = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        a = i * j
        if (palindrom(a) and a > maximum):
            maximum = a

print(maximum)
