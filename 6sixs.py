sumk = 0
ksum = 0
for i in range(1, 101):
    sumk += i ** 2
    ksum += i
ksum = ksum ** 2
print(ksum - sumk)
