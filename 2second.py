i = 0
x = 1
y = 1
Result = 0
while (i <= 4000000):
    i = x + y
    if (i % 2 == 0 and i <= 4000000):
        Result += i
    x = y
    y = i
print(Result)
