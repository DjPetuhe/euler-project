i = 3
Result = 0
while (i < 1000):
    if (i % 3 == 0 or i % 5 == 0):
        Result += i
    i += 1
print(Result)
